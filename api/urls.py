from django.urls import path
from api.question_api import question_list


urlpatterns = [
    path('question_list/', question_list)
]
