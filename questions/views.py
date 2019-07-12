from django.shortcuts import render, get_object_or_404
from django.views import View

from questions.models import Question, Statistics

from random import choice


class QuestionView(View):

    def get(self, request):
        answered = set(request.session.get('answered', []))
        questions = set(Question.objects.values_list('id', flat=True))
        not_answered = list(questions - answered)
        try:
            question_id = choice(not_answered)
            request.session['question'] = question_id
            q = Question.objects.get(id=question_id)
            return render(request, 'question.html', {'question': q})

        except IndexError:
            return render(request, 'empty.html')

    def post(self, request):
        question = get_object_or_404(Question, id=request.session.get('question'))
        del request.session['question']
        answer_id = int(request.POST.get('answer'))
        answered_questions = request.session.get('answered', [])
        answered_questions.append(question.id)
        request.session['answered'] = answered_questions
        correct_id = question.correct_answer.id
        stat, created = Statistics.objects.get_or_create(question=question, defaults={
            'answered': 1,
            'correctly': 1 if answer_id == correct_id else 0
        })

        if not created:
            stat.answered += 1
            if answer_id == correct_id:
                stat.correctly += 1

        stat.save()

        return render(request, 'result.html', dict(question=question, correct=correct_id, answered=answer_id))
