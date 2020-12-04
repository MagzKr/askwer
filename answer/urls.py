from django.urls import path
from answer.views import create_answer

urlpatterns = [
    path('create_answer/', create_answer, name='create_answer'),
]
