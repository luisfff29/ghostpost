from django import forms
from ghostpost_app.models import GhostModel


class GhostForm(forms.ModelForm):
    class Meta:
        model = GhostModel
        fields = ['text', 'boast_or_roast']
