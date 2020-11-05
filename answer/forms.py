from  django import forms
from  .models import Answer
from django.shortcuts import redirect

class AnswerForm(forms.ModelForm):
    class Meta:
        model = Answer
        fields = ['text']


