from django.shortcuts import render, get_object_or_404
from question.models import Question
from .forms import QuestionForm
from django.contrib.auth.decorators import login_required
from django.http import HttpResponseRedirect
from answer.views import get_answers
from django.core.paginator import Paginator, PageNotAnInteger


def question_list_view(request):
    question_list = Question.objects.new()
    page = request.GET.get('page', 1)
    paginator = Paginator(question_list, 10)
    try:
        questions = paginator.page(page)
    except PageNotAnInteger:
        questions = paginator.page(1)

    context = {'question_list':questions}
    return render(request, 'question/question_list.html', context)


def question_details(request, pk):
    question = get_object_or_404(Question, pk=pk)
    answers = get_answers(pk)
    context = {
        'question': question,
        'answers': answers,
    }

    return render(request, 'question/question_details.html', context)


@login_required
def create_question(request):
    question_form = QuestionForm(request.POST)
    if question_form.is_valid():
        new_question = question_form.save(commit=False)
        new_question.author = request.user
        new_question.save()
        return HttpResponseRedirect(new_question.get_url())

@login_required
def ask_question(request):
    question_form = QuestionForm()
    if request.method == 'POST':
        return create_question(request)

    context = {
        'question_form': question_form
    }
    return render(request, 'question/ask_question.html', context)

