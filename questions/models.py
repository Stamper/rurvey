from django.db import models


class Question(models.Model):
    title = models.TextField()

    @property
    def correct_answer(self):
        return self.answers.filter(correct=True).first()

    def __str__(self):
        return 'Question: {} (answers: {})'.format(self.title[0:99], self.answers.count())


class Answer(models.Model):
    question = models.ForeignKey('questions.Question', related_name='answers', on_delete=models.CASCADE)
    answer = models.TextField()
    correct = models.BooleanField()


class Statistics(models.Model):
    question = models.ForeignKey('questions.Question', related_name='statistics', on_delete=models.CASCADE)
    answered = models.BigIntegerField()
    correctly = models.BigIntegerField()

    class Meta:
        verbose_name_plural = 'Statistics'
