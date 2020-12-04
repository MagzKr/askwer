from django.shortcuts import render
from question.models import Question
from answer.models import Answer
from .forms import QuestionForm
from django.contrib.auth.decorators import login_required
from django.http import HttpResponseRedirect, JsonResponse
from django.core.paginator import Paginator, PageNotAnInteger
import random


def question_list_view(request):
    if request.GET.get('tag'):
        question_list = Question.objects.get_tag(request.GET['tag'])
        page_title = request.GET['tag'].capitalize()
    else:
        question_list = Question.objects.new()
        page_title = 'New Questions'
    page = request.GET.get('page', 1)
    paginator = Paginator(question_list, 10)
    try:
        questions = paginator.page(page)
    except PageNotAnInteger:
        questions = paginator.page(1)

    context = {
        'question_list': questions,
        'page_title': page_title,
        'page_type': 'question_list'  # changing type of stats container and num of visible chars of question.text
    }
    return render(request, 'question/question_list.html', context)


def question_details(request, pk):
    question = Question.objects.select_related('author').get(pk=pk)
    answers = Answer.objects.get_answers(pk)
    context = {
        'question': question,
        'answers': answers,
        'page_type': 'question_details'
    }

    return render(request, 'question/question_details.html', context)


@login_required
def create_question(request):
    question_form = QuestionForm(request.POST)
    if question_form.is_valid():
        new_question = question_form.save(commit=False)
        new_question.author = request.user
        new_question.save()
        for tag in request.POST['tags'].split():
            new_question.tags.add(tag.strip(',.* '))
        return HttpResponseRedirect(new_question.get_url())


@login_required
def ask_question(request):
    question_form = QuestionForm()
    if request.method == 'POST':
        return create_question(request)

    context = {
        'question_form': question_form
    }
    return render(request, 'question/ask_question.html', context)


@login_required
def rate_question(request):
    if request.user.is_authenticated:
        question = Question.objects.prefetch_related('likes', 'dislikes').get(pk=request.POST.get('questionPk'))
    else:
        return JsonResponse({'response': 'User is not authenticated'})

    if request.POST.get('method') == 'up':
        if request.user not in question.likes.all():
            question.rating += 1
            if request.user in question.dislikes.all():
                question.dislikes.remove(request.user)
            else:
                question.likes.add(request.user)
            question.save()
            return JsonResponse({'response': 'Success', 'rating': question.rating})

    if request.POST.get('method') == 'down':
        if request.user not in question.dislikes.all():
            question.rating -= 1
            if request.user in question.likes.all():
                question.likes.remove(request.user)
            else:
                question.dislikes.add(request.user)
            question.save()
            return JsonResponse({'response': 'Success', 'rating': question.rating})


def add_random_question(request):
    for i in range(100):
        text = 'itertools.product will generate all the possible values. Instead, what you want is to pick n random ' \
               'characters from chrs and concatenate them '
        tags = ['python', 'js', 'django', 'java', 'sql', 'css', 'html']
        words = text.split()
        new_question = Question()
        new_question.title = ' '.join(random.choices(words, k=4))
        new_question.author = request.user
        new_question.text = ' '.join(random.choices(words, k=20))
        new_question.rating = random.randint(-100, 100)
        new_question.save()
        for _ in range(random.randint(0, len(tags))):
            new_question.tags.add(random.choice(tags))
    return JsonResponse({'Response': 'OK'})
