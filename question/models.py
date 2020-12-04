from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User
from taggit.managers import TaggableManager
from django.urls import reverse


class Question_manager(models.Manager):
    def new(self):
        return self.select_related('author').order_by('-added_at')

    def popular(self):
        return self.select_related('author').order_by('-rating')

    def get_tag(self, tag):
        return self.select_related('author').filter(tags__name__in=[tag]).order_by('-added_at')


class Question(models.Model):
    title = models.CharField(max_length=255)
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    text = models.TextField()
    added_at = models.DateTimeField(default=timezone.now)
    rating = models.IntegerField(default=0)
    likes = models.ManyToManyField(User, related_name='Users_liked_question', blank=True)
    dislikes = models.ManyToManyField(User, related_name='Users_disliked_question', blank=True)
    objects = Question_manager()
    tags = TaggableManager()

    def get_url(self):
        return reverse('question_detail_view', args=[str(self.pk)])

    def __str__(self):
        return self.title
