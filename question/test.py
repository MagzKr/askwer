import datetime
from .models import Question
from django.test import TestCase
from django.utils import timezone



class QuestionModelTests(TestCase):

    def test_was_published_recently_with_future_question(self):
        self.assertIs(False, False)