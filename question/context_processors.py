from question.models import Question


def get_tags(request):
    return {'all_tags': Question.tags.all()}
