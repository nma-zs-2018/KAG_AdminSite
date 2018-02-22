from django.db import models

# Create your models here.


class Lesson(models.Model):
    start = models.TimeField()
    duration = models.IntegerField(default=45)


class PollData(models.Model):
    id = models.CharField(max_length=10)
    timestamp = models.CharField(max_length=30)
