from django import forms
from ghostpost_app.models import GhostPost


class AddPost(forms.ModelForm):
    class Meta:
        model = GhostPost
        fileds = '__all__'

# class GhostPost(models.Model):
#     text = models.CharField(max_length=280)
#     choice = models.BooleanField(help_text='Check: Boast, Uncheck: Roast')
#     up_vote = models.IntegerField(default=0)
#     down_vote = models.IntegerField(default=0)
#     date = models.DateTimeField(default=timezone.now)
