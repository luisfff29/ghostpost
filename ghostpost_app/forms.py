from django import forms
from ghostpost_app.models import GhostPost


class AddPost(forms.ModelForm):
    class Meta:
        model = GhostPost
        fields = ['text', 'boast_or_roast']
