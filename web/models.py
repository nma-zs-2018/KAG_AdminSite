from django.db import models

# Create your models here.


class Lesson(models.Model):
    start = models.TimeField()
    duration = models.IntegerField(default=45)
