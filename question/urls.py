from django.urls import path
from question.views import question_list_view, question_details, ask_question, rate_question, add_random_question
urlpatterns = [
    path('', question_list_view, name='question_list_view'),
    path('ask/', ask_question, name='ask_question'),
    path('rate/', rate_question, name='rate_question'),
    path('random/', add_random_question),
    path('<int:pk>', question_details, name='question_detail_view'),
]
