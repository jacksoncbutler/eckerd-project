from django.db import models
from multiselectfield import MultiSelectField

DAYS_OF_WEEK = (
    (0, 'Sunday'),
    (1, 'Monday'),
    (2, 'Tuesday'),
    (3, 'Wednesday'),
    (4, 'Thursday'),
    (5, 'Friday'),
    (6, 'Saturday'),
)

class Class(models.Model):
    name = models.CharField(max_length=250)
    code = models.CharField(max_length=15)
    teacher = models.CharField(max_length=100,)
    days = MultiSelectField(choices=DAYS_OF_WEEK, max_choices=7)
    start = models.TimeField(max_length=5, default='12:00')
    end = models.TimeField(max_length=5, default='12:00')
    description = models.TextField(max_length=2000)

