from django.db import models
from django.contrib.auth.models import User
from question.models import Question


class AnswerManager(models.Manager):

    def get_answers(self, pk):
        return self.filter(question=pk)


class Answer(models.Model):
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    text = models.TextField()
    added_at = models.DateTimeField(auto_now_add=True)
    question = models.ForeignKey(Question, on_delete=models.CASCADE)
    objects = AnswerManager()

    class Meta:
        ordering = ['-added_at']
