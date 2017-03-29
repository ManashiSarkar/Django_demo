from django import forms
from django.contrib.auth.models import User

class Signup(forms.Form):
	First_name = forms.CharField(label='First name',required=True,max_length=20)
	Last_name = forms.CharField(label='Last name',required=True,max_length=20)
	
	def signup(self, request, user):
		user.first_name = self.cleaned_data['First_name']
		user.last_name = self.cleaned_data['Last_name']
		user.save()