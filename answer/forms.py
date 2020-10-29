from  django import forms
from  .models import Answer

class AnswerForm(forms.ModelForm):
    answer_text = forms.Textarea()
    class Meta:
        model = Answer
        fields = ['text']
