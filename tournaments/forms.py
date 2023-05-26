from django import forms
from .models import Team, Match


class TeamForm(forms.ModelForm):
    class Meta:
        model = Team
        fields = ['name', 'description', 'players']
        widgets = {
            'players': forms.CheckboxSelectMultiple
        }


class MatchResultForm(forms.ModelForm):
    class Meta:
        model = Match
        fields = ['winner']
