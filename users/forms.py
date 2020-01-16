# users/forms.py

from django import forms
from django.contrib.auth.forms import UserCreationForm, UserChangeForm

from .models import CustomUser

class CustomUserCreationForm(UserCreationForm):

    class Meta(UserCreationForm.Meta):
        model = CustomUser
        fields = ('email', 'username', 'first_name', 'last_name', 'gender', 'date_of_birth', 'department', 'year_in_school', 'I_can_program', 'why_join_HEX',)

class CustomUserChangeForm(UserChangeForm):

    class Meta:
        model = CustomUser
        fields = ('email', 'username', 'first_name', 'last_name', 'gender', 'date_of_birth', 'department', 'year_in_school', 'I_can_program', 'why_join_HEX',)
