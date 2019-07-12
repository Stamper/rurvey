from django.contrib import admin

from questions.forms import AnswersInlineFormSet
from questions.models import Question, Answer, Statistics


class AnswersInline(admin.StackedInline):
    formset = AnswersInlineFormSet
    model = Answer
    extra = 1


@admin.register(Question)
class QuestionAdmin(admin.ModelAdmin):
    inlines = [AnswersInline, ]


@admin.register(Statistics)
class StatisticsAdmin(admin.ModelAdmin):
    list_display = ('question', 'answered', 'correctly')

    def has_add_permission(self, request):
        return False
