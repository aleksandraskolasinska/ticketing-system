from django import forms
from .models import Ticket
from django.contrib.auth.forms import UserCreationForm, PasswordChangeForm, UserChangeForm
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

# class AccountForm(UserChangeForm):
#     password_change = PasswordChangeForm

#     class Meta(UserChangeForm.Meta):
#         fields = ['username', 'email', 'first_name', 'last_name']

# Change User details

class UsernameUpdateForm(forms.Form):
    new_username = forms.CharField(max_length=150)

class PasswordUpdateForm(forms.Form):
    current_password = forms.CharField(widget=forms.PasswordInput)
    new_password = forms.CharField(widget=forms.PasswordInput)
    confirm_password = forms.CharField(widget=forms.PasswordInput)

class EmailUpdateForm(forms.Form):
    new_email = forms.EmailField()

class FirstNameUpdateForm(forms.Form):
    new_first_name = forms.CharField(max_length=150)

class LastNameUpdateForm(forms.Form):
    new_last_name = forms.CharField(max_length=150)