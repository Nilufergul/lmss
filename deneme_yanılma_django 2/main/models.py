from django.db import models


class Student (models.Model):
    name = models.CharField(max_length=200)
    grade = models.IntegerField()
    field = models.CharField(max_length=200)
    school_number = models.IntegerField()
    email = models.EmailField()

    def __str__(self):
        return self.name


class Lesson(models.Model):
    EVENT_TYPE_CHOICES = [
        ('event', 'Genel Etkinlik'),
        ('exam', 'Sınav'),
        ('assignment', 'Ödev'),
    ]
    lesson_name = models.CharField(max_length=200)
    field = models.CharField(max_length=200)  # çap öğrencileri için opsiyonel
    year = models.ForeignKey(Student, on_delete=models.CASCADE)  # optional
    event_type = models.CharField(max_length=20, choices=EVENT_TYPE_CHOICES)

    def get_event_color(self):
        # Etkinlik türüne göre renk döndür
        if self.event_type == 'event':
            return 'blue'
        elif self.event_type == 'exam':
            return 'red'
        elif self.event_type == 'assignment':
            return 'green'
        else:
            return 'black'

    def __str__(self):
        return self.name + ' added at ' + str(self.year)


class Notes(models.Model):
    lesson = models.ForeignKey(Lesson, on_delete=models.CASCADE)
    week = models.IntegerField()
    title = models.TextField()

    def __str__(self):
        return self.title
