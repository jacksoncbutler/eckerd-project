from django.db import models
from multiselectfield import MultiSelectField



class Class(models.Model):
    DAYS_OF_WEEK = (
        (0, 'Sunday'),
        (1, 'Monday'),
        (2, 'Tuesday'),
        (3, 'Wednesday'),
        (4, 'Thursday'),
        (5, 'Friday'),
        (6, 'Saturday'),
    )

    name = models.CharField(max_length=250)
    code = models.CharField(max_length=15)
    teacher = models.CharField(max_length=100,)
    days = MultiSelectField(choices=DAYS_OF_WEEK, max_choices=7)
    start = models.TimeField(max_length=5, default='00:00')
    end = models.TimeField(max_length=5, default='24:00')
    description = models.TextField(max_length=2000)


class Article(models.Model):
    ARTICLE_TYPE = (
        ('news_article', 'News Article'),
        ('announcement', 'Announcement')
    )
    article_type = models.CharField(max_length=40, choices=ARTICLE_TYPE)
    title = models.CharField(max_length=150)
    author = models.CharField(max_length=100)
    description = models.CharField(max_length=500)
    url = models.CharField(max_length=250)

    def get_absolute_url(self):
        return reverse('music:detail', kwargs={'pk': self.pk})


# class Calendar(models.Model):
#
#
#
#
# class Week(models.Model):
#
#
#
# class Day(models.Model):
#
#
#
# class Event(models.Model):
#     name = models.CharField(max_length=100)
#     location = models.CharField(max_length=300, required=False)
#     all_day = models.BooleanField(default=False)
#     if all_day:
#         start = '00:00'
#         end = '24:00'
#     else:
#         start = models.TimeField(max_length=5, default='00:00')
#         end = models.TimeField(max_length=5, default='24:00')