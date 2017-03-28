from django import forms
from django.contrib.auth.models import User

class Signup(forms.Form):
	First_name = forms.CharField(label='first_name',required=True,max_length=20)
	Last_name = forms.CharField(label='last_name',required=True,max_length=20)
	
	def signup(self, request, user):
		user.First_name = self.First_name
		user.Last_name = self.Last_name