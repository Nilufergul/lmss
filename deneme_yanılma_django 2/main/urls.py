from django.urls import path
from main.views import create_lesson

urlpatterns = [
    path('create_lesson', create_lesson, name='create_lesson'),
]