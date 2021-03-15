from django.core.paginator import Paginator
from django.db.models import Q, Count
from django.shortcuts import render, get_object_or_404

from ..models import Question


def index(request):
    3/0
    """
    pybo 목록 출력
    """
    # 입력 파라미터
    page = request.GET.get('page', '1')  # 페이지
    kw = request.GET.get('kw', '')
    so = request.GET.get('so', 'recent')
    ca = request.GET.get('ca', 'quest')

    # 정렬
    if so == 'recommend':
        question_list = Question.objects.annotate(num_voter=Count('voter')).order_by('-num_voter', '-create_date')
    elif so == 'popular':
        question_list = Question.objects.annotate(num_answer=Count('answer')).order_by('-num_answer', '-create_date')
    else:  # recent
        question_list = Question.objects.order_by('-create_date')

    # 조회
    if kw:
        question_list = question_list.filter(
            Q(subject__icontains=kw)|
            Q(content__icontains=kw)|
            Q(author__username__icontains=kw)|
            Q(answer__author__username__icontains=kw)
        ).distinct()

    if ca:
        question_list = question_list.filter(
            Q(category__icontains=ca)
        ).distinct()

    # 페이징처리
    paginator = Paginator(question_list, 10)  # 페이지당 10개씩 보여주기
    page_obj = paginator.get_page(page)

    context = {'question_list': page_obj, 'page': page, 'kw': kw, 'so': so, 'ca': ca}
    return render(request, 'pybo/question_list.html', context)

def detail(request, question_id):
    """
    pybo 게시글 상세정보 및 답글 출력
    """
    page = request.GET.get('page', '1')  # 페이지
    so = request.GET.get('so', 'recent')
    question = get_object_or_404(Question, pk=question_id)
    if so == 'recommend':
        answer_list = question.answer_set.annotate(num_voter=Count('voter')).order_by('-num_voter', '-create_date')
    else:
        answer_list = question.answer_set.order_by('-create_date')
    paginator = Paginator(answer_list, 5)  # 페이지당 5개씩 보여주기
    page_obj = paginator.get_page(page)
    context = {'question': question, 'answer_list': page_obj, 'page': page, 'so': so}
    return render(request, 'pybo/question_detail.html', context)