import pytest
import datetime
from poll.models import Question
from django.utils import timezone
from django.test import TestCase
from django.http import status

@pytest.mark.django_db
class TestQuestionModel:
    def test_was_published_recently_with_future_question(self):
        time=timezone.now()+datetime.timedelta(days=30)
        future_question = Question(pub_date=time)
        if future_question == False:
            assert future_question.data is False
        