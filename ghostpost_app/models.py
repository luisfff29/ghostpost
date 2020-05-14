from django.db import models
from django.utils import timezone


# Create your models here.
class GhostPost(models.Model):
    text = models.CharField(max_length=280)
    choice = models.BooleanField(help_text='Check: Boast, Uncheck: Roast')
    up_vote = models.IntegerField(default=0)
    down_vote = models.IntegerField(default=0)
    date = models.DateTimeField(default=timezone.now)

    def __str__(self):
        return self.choice
