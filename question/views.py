from django.shortcuts import render, get_object_or_404
from question.models import Question
from answer.forms import AnswerForm
from answer.models import Answer
from answer.views import create_answer
# Create your views here.

def Question_list_view(request):
    question_list = Question.objects.new()
    context = {'question_list':question_list}
    return render(request, 'question/question_list.html', context)

def Question_details(request, pk):
    question = get_object_or_404(Question, pk=pk)
    answers = Answer.objects.filter(question=pk)
    answer_form = AnswerForm()

    if request.method == 'POST':
        create_answer(request,question)

    context = {
        'question': question,
        'answers': answers,
        'answer_form': answer_form}
    return render(request, 'question/question_details.html', context)
