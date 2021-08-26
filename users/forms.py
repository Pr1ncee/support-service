from django import forms

from .models import Ticket


class TicketForm(forms.ModelForm):
    class Meta:
        model = Ticket
        fields = ['message']
        labels = {'text': ''}
        widgets = {'text': forms.Textarea()}
