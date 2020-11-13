from django.urls import path
from answer.views import create_answer, get_answers


urlpatterns = [path('create_answer/', create_answer, name='create_answer'),
               path('get_answers/',get_answers, name='get_answers')
               ]