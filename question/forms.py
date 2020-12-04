from django import forms
from .models import Question


class QuestionForm(forms.ModelForm):
    class Meta:
        model = Question
        fields = ['title', 'text', 'tags']

    def clean_title(self):
        title = self.cleaned_data['title']
        return title[0].upper() + title[1:].lower()

    def clean_text(self):
        text = self.cleaned_data['text']
        return text[0].upper() + text[1:].lower()

    def clean_tags(self):
        text = self.cleaned_data['tags']
