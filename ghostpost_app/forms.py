from django import forms
from ghostpost_app.models import GhostModel


class GhostForm(forms.ModelForm):
    text = forms.CharField(widget=forms.Textarea(
        attrs={
            'placeholder': 'Enter text here...',
            'class': 'form-control'
        }))

    class Meta:
        model = GhostModel
        fields = ['boast_or_roast', 'text']
