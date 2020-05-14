from django.db import models
from django.utils import timezone


# Create your models here.
BOOL_CHOICES = ((True, 'Boast'), (False, 'Roast'))


class GhostModel(models.Model):
    text = models.CharField(max_length=280)
    boast_or_roast = models.BooleanField(choices=BOOL_CHOICES, null=False)
    up_vote = models.IntegerField(default=0)
    down_vote = models.IntegerField(default=0)
    date = models.DateTimeField(default=timezone.now)

    def __str__(self):
        return 'Boast' if self.boast_or_roast else 'Roast'
