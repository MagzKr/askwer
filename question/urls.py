from django.urls import path
from question.views import Question_list_view, Question_details
urlpatterns = [
    path('',Question_list_view, name='question_list_view'),
    path('<pk>', Question_details, name='question_detail_view' )
]