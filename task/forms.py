from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
from task.models import *


# this is the user registration form
class RegisterForm(UserCreationForm):
	first_name = forms.CharField(max_length=50, required=True)
	last_name = forms.CharField(max_length=50, required=True)
	email = forms.EmailField(required=True)

	class Meta():
		model = User
		fields = ['first_name', 'last_name', 'email', 'username', 'password1', 'password2']


class TaskCreationForm(forms.ModelForm):
	class Meta():
		model = Task
		fields = ['title', 'description', 'complete']