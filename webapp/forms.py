#

from django import forms


class ClinicTicketForm(forms.Form):
    clinic = forms.ChoiceField(
        widget=forms.Select(attrs={'class': 'form-control'})
    )
    description = forms.CharField(
        widget=forms.Textarea(attrs={'class': 'form-control'})
    )
