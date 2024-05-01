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



def loginPage(request):
    return render(request, 'login.html')

def dashboardPage(request):
    return render(request, 'dashboard.html')

def userPage(request):
    return render(request, 'user.html')

def myLessonsPage(request):
    return render(request, 'mylessons.html')

def calenderPage(request):
    return render(request, 'calender.html')

def notesPage(request):
    return render(request, 'notes.html')

def announcementsPage(request):
    return render(request, 'announcements.html')

def settingsPage(request):
    return render(request, 'settings.html')

def sidebar(request):
    return render(request, 'sidebar.html')
