from django import forms
from ghostpost_app.models import GhostModel


CHOICES = ((('---------', '---------')), ('all_boasts', 'All Boasts'), ('all_roasts', 'All Roasts'),
           ('up_vote', 'Up votes'), ('down_vote', 'Down votes'), ('vote_difference', 'Vote difference'))


class GhostForm(forms.ModelForm):
    text = forms.CharField(widget=forms.Textarea(
        attrs={
            'placeholder': 'Enter text here...',
            'class': 'form-control'
        }))

    class Meta:
        model = GhostModel
        fields = ['boast_or_roast', 'text']


class AddFilter(forms.Form):
    add_filter = forms.ChoiceField(choices=CHOICES, widget=forms.Select(
        attrs={
            'onchange': 'submit()'
        }
    ))
