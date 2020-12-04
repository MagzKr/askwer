from django.test import TestCase
from question.models import Question
from answer.models import Answer
from django.urls import reverse
from django.contrib.auth.models import User


class QuestionListViewTest(TestCase):
    @classmethod
    def setUpTestData(cls):
        number_of_questions = 100
        user = User.objects.create_user(username='TestUser')
        for question_num in range(number_of_questions):
            Question.objects.create(pk=question_num, author=user, title='TestTitle', text='TestText')
        test_question = Question.objects.get(pk=1)
        test_question.tags.add('testtag')

    def test_view_url_exists_at_desired_location(self):
        resp = self.client.get('/')
        self.assertEqual(resp.status_code, 200)

    def test_view_uses_correct_template(self):
        resp = self.client.get(reverse('question_list_view'))
        self.assertEqual(resp.status_code, 200)
        self.assertTemplateUsed(resp, 'question/question_list.html')

    def test_pagination_is_ten(self):
        resp = self.client.get(reverse('question_list_view'))
        self.assertEqual(resp.status_code, 200)
        self.assertTrue('question_list' in resp.context)
        self.assertTrue(len(resp.context['question_list']) == 10)

    def test_tag_on_top_page(self):
        resp = self.client.get(reverse('question_list_view') + '?tag=testtag')
        self.assertEqual(resp.status_code, 200)
        self.assertTrue(resp.context['page_title'] == 'Testtag')

    def test_question_tag_filter(self):
        question = Question.objects.get_tag('testtag')[0]
        resp = self.client.get(reverse('question_list_view') + '?tag=testtag')
        self.assertEquals(question.tags.all()[0], resp.context['question_list'][0].tags.all()[0])

    def test_page_type(self):
        resp = self.client.get(reverse('question_list_view'))
        self.assertTrue(resp.context['page_type'] == 'question_list')


class QuestionDetailsViewTest(TestCase):
    @classmethod
    def setUpTestData(cls):
        user = User.objects.create_user(username='TestUser')
        question = Question.objects.create(pk=1, author=user, title='TestTitle', text='TestText')
        Answer.objects.create(author=user, text='TestText', question=question)

    def test_view_url_exists_at_desired_location(self):
        resp = self.client.get('/question/1')
        self.assertEqual(resp.status_code, 200)

    def test_view_use_correct_template(self):
        resp = self.client.get(reverse('question_detail_view', args='1'))
        self.assertEqual(resp.status_code, 200)
        self.assertTemplateUsed(resp, 'question/question_details.html')

    def test_answers_is_show(self):
        resp = self.client.get(reverse('question_detail_view', args='1'))
        self.assertEqual(resp.status_code, 200)
        self.assertTrue(len(resp.context['answers']) == 1)

    def page_type_test(self):
        resp = self.client.get(reverse('question_detail_view', args='1'))
        self.assertTrue(resp.context['page_type'] == 'question_details')
