from django import forms
from .models import Ticket
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User

class TicketForm(forms.ModelForm):
    class Meta:
        model = Ticket
        fields = ['title', 'ticket_content']

class SignUpForm(UserCreationForm):
    email = forms.EmailField()

    class Meta:
        model = User
        fields = ['username', 'email', 'password1', 'password2']

