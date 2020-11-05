from django.urls import path
from question.views import question_list_view, question_details, ask_question
urlpatterns = [
    path('', question_list_view, name='question_list_view'),
    path('<pk>', question_details, name='question_detail_view'),
    path('ask/', ask_question, name='ask_question')
]