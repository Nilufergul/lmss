from django import forms
from main.models import Lesson, Notes


class LessonForm(forms.Form):
    name = forms.CharField(max_length=200)
    field = forms.CharField(max_length=200)
    year = forms.IntegerField(min_value=1, max_value=6)
    event_type = forms.CharField(max_length=200)

    # release_date = forms.DateField(widget=forms.DateInput(attrs={'type': 'date'}))


class NotesForm(forms.Form):
    Lesson = forms.ModelChoiceField(queryset=Lesson.objects.all())
    week = forms.IntegerField(min_value=1, max_value=14)
    note = forms.CharField(widget=forms.Textarea)
