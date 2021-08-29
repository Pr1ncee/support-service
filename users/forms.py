from django import forms

from .models import Ticket, Answer


class TicketForm(forms.ModelForm):
    class Meta:
        model = Ticket
        fields = ['message']
        labels = {'text': ''}
        widgets = {'text': forms.Textarea()}


class AnswerForm(forms.ModelForm):
    class Meta:
        model = Answer
        fields = ['answer']
        labels = {'text': ''}
        widgets = {'text': forms.Textarea()}
