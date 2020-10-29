from django.shortcuts import render
from .forms import AnswerForm
# Create your views here.
def create_answer(request, question):
    answer_form = AnswerForm(data=request.POST)
    if answer_form.is_valid():
        new_answer = answer_form.save(commit=False)
        new_answer.question = question
        new_answer.author = request.user
        new_answer.save()
    return answer_form

