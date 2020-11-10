from .models import Answer
from question.models import Question
from django.contrib.auth.models import User
from django.shortcuts import render
from django.http import HttpResponseBadRequest

def text_valid(text):
    if text != '':
        return True
    else:
        return False


def create_answer(request):
        new_answer = Answer()
        if request.user.is_authenticated:
            new_answer.author = request.user
        else:
            new_answer.author = User.objects.get(username='Guest')
        new_answer.question = Question.objects.get(pk=request.POST.get('questionPk'))
        new_answer.text = request.POST.get('text')
        if text_valid(new_answer.text):
            new_answer.save()
            return render(request, 'answer/single_answer.html', {'answer':new_answer})
        else:
            error = b'You give bad answer!'
            return HttpResponseBadRequest(error)


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


