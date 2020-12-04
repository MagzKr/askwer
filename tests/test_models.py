from question.models import Question
from django.test import TestCase
from django.contrib.auth.models import User
from answer.models import Answer
import datetime
import pytz


class QuestionModelTests(TestCase):
    @classmethod
    def setUpTestData(cls):
        user = User.objects.create(username='TestUser')
        tags = ['python', 'django']
        test_question = Question()
        test_question.title = 'TestTitle'
        test_question.author = user
        test_question.text = 'TestText'
        test_question.rating = 0
        test_question.added_at = datetime.datetime(2020, 4, 4, 0, 0, 0, tzinfo=pytz.utc)
        test_question.save()
        for tag in tags:
            test_question.tags.add(tag)

    def test_field_title(self):
        test_question = Question.objects.get(pk=1)
        field_label = test_question._meta.get_field('title').verbose_name
        max_length = test_question._meta.get_field('title').max_length
        self.assertEquals(field_label, 'title')
        self.assertEquals(max_length, 255)

    def test_field_author(self):
        test_question = Question.objects.get(pk=1)
        field_label = test_question._meta.get_field('author').verbose_name
        self.assertEquals(field_label, 'author')

    def test_field_text(self):
        test_question = Question.objects.get(pk=1)
        field_label = test_question._meta.get_field('text').verbose_name
        self.assertEquals(field_label, 'text')

    def test_field_added_at(self):
        test_question = Question.objects.get(pk=1)
        field_label = test_question._meta.get_field('added_at').verbose_name
        self.assertEqual(test_question.added_at, datetime.datetime(2020, 4, 4, 0, 0, 0, tzinfo=pytz.utc))
        self.assertEquals(field_label, 'added at')

    def test_field_rating(self):
        test_question = Question.objects.get(pk=1)
        field_label = test_question._meta.get_field('rating').verbose_name
        self.assertEquals(field_label, 'rating')

    def test_field_likes(self):
        test_question = Question.objects.get(pk=1)
        field_label = test_question._meta.get_field('likes').verbose_name
        self.assertEquals(field_label, 'likes')

    def test_field_dislikes(self):
        test_question = Question.objects.get(pk=1)
        field_label = test_question._meta.get_field('dislikes').verbose_name
        self.assertEquals(field_label, 'dislikes')

    def test_field_tags(self):
        test_question = Question.objects.get(pk=1)
        field_label = test_question._meta.get_field('tags').verbose_name
        self.assertEquals(field_label, 'Tags')

    def test_get_url(self):
        test_question = Question.objects.get(pk=1)
        self.assertEquals(test_question.get_url(), '/question/1')

    def test_object_name_is_title(self):
        test_question = Question.objects.get(pk=1)
        self.assertEquals(str(test_question), 'TestTitle')


class AnswerModelTests(TestCase):
    @classmethod
    def setUpTestData(cls):
        user = User.objects.create(username='TestUser')
        question = Question.objects.create(author=user, pk=1)
        test_answer = Answer()
        test_answer.author = user
        test_answer.text = 'TestText'
        test_answer.question = question
        test_answer.added_at = datetime.datetime(2020, 4, 4, 0, 0, 0, tzinfo=pytz.utc)
        test_answer.save()

    def test_field_author(self):
        test_answer = Answer.objects.get_answers(pk=1)[0]
        field_label = test_answer._meta.get_field('author').verbose_name
        self.assertEquals(field_label, 'author')
        self.assertEquals(test_answer.author.username, 'TestUser')

    def test_field_text(self):
        test_answer = Answer.objects.get_answers(pk=1)[0]
        field_label = test_answer._meta.get_field('text').verbose_name
        self.assertEquals(field_label, 'text')
        self.assertEquals(test_answer.text, 'TestText')

    def test_field_added_at(self):
        test_answer = Answer.objects.get_answers(pk=1)[0]
        field_label = test_answer._meta.get_field('added_at').verbose_name
        self.assertEquals(field_label, 'added at')

    def test_field_question(self):
        test_answer = Answer.objects.get_answers(pk=1)[0]
        question = Question.objects.get(pk=1)
        self.assertEquals(question.pk, test_answer.question.pk)
