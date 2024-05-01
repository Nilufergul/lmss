from django.urls import path
from register.views import register
from . import views

urlpatterns = [
    path('register/register', register, name='register'),
    path("", views.loginPage, name="login page"),
    path("dashboard" , views.dashboardPage, name="dashboard page"),
    path("user", views.userPage, name="user page"),
    path("mylessons", views.myLessonsPage, name="my lessons page"),
    path("calender", views.calenderPage, name="calender page"),
    path("notes", views.notesPage, name="notes page"),
    path("announcements", views.announcementsPage, name="announcements page"),
    path("settings", views.settingsPage, name="settings page"),
    path("sidebar", views.sidebar, name="settings page")
]