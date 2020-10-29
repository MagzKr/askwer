from django.shortcuts import render, get_object_or_404
from question.models import Question
# Create your views here.

def Question_list_view(request):
    question_list = Question.objects.new()
    context = {'question_list':question_list}
    return render(request, 'question/question_list.html', context)

def Question_details(request, pk):
    question = get_object_or_404(Question, pk=pk)
    context = {'question':question}
    return render(request, 'question/question_details.html', context)