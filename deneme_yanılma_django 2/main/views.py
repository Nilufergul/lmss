from django.db import transaction
from django.shortcuts import render, redirect
from django.http import HttpResponse
from main.models import Lesson, Student, Notes
from main.forms import LessonForm, NotesForm


# @transaction.atomic() !!!!
def create_lesson(request):
    if request.method == 'POST':
        form = LessonForm(request.POST)
        if form.is_valid():
            lesson = Lesson()
            lesson.name = form.cleaned_data['name']
            lesson.field = form.cleaned_data['field']
            lesson.year = form.cleaned_data['year']
            lesson.event_type = form.cleaned_data['event_type']
            lesson.save()
            return redirect('my_lessons')
    else:  # request.method is a GET (the first time get)
        form = LessonForm()

    return render(request, 'lesson.html', context={'form': form})


def my_lessons(request):
    lessons = Lesson.objects.all()

