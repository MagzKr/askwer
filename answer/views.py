from .models import Answer
from question.models import Question
from django.contrib.auth.models import User

def create_answer(request):
        new_answer = Answer()
        print(request.POST)
        if request.user.is_authenticated:
            new_answer.author = request.user
        else:
            new_answer.author = User.objects.get(username='Guest')
        new_answer.question = Question.objects.get(pk=request.POST.get('questionPk'))
        new_answer.text = request.POST.get('text')
        new_answer.save()
        return None


def get_answers(pk):
    return Answer.objects.filter(question=pk)


# def likePost(request):
#     if request.method == 'GET':
#             post_id = request.GET['post_id']
#             likedpost = Post.objects.get(pk=post_id)  # getting the liked posts
#             m = Like(post=likedpost)  # Creating Like Object
#             m.save()  # saving it to store in database
#             return HttpResponse("Success!")  # Sending an success response
#     else:
#             return HttpResponse("Request method is not a GET")
# def new_answers():


