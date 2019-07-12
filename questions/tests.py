from django.test import TestCase

from questions.models import Question

from model_mommy import mommy


class TestQuestionModel(TestCase):
    def test_correct_answer(self):
        q = mommy.make('questions.Question')
        mommy.make('questions.Answer', question=q, correct=False, _quantity=3)
        correct = mommy.make('questions.Answer', question=q, correct=True)
        self.assertEqual(q.correct_answer, correct)
