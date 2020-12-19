from django.http import JsonResponse
from question.models import Question
from question.serializers import QuestionSerializer


def question_list(request):
    if request.method == 'GET':
        questions = Question.objects.new()
        serializer = QuestionSerializer(questions, many=True)
        return JsonResponse(serializer.data, safe=False)