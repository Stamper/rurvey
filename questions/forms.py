from django import forms


class AnswersInlineFormSet(forms.BaseInlineFormSet):
    def clean(self):
        not_empty_answers = [x for x in self.cleaned_data if x]
        correct_answers = [y for y in not_empty_answers if y.get('correct')]

        if not len(not_empty_answers):
            raise forms.ValidationError('Question must contain at least one answer')

        if not len(correct_answers) == 1:
            raise forms.ValidationError('There must be one correct answer')

        return self.cleaned_data
