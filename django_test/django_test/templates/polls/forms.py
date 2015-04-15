from django import forms

class LoginForm(forms.Form)
	username = forms.CharField(label='User name', max_length=100)
	password = forms.CharField(widget=forms.PasswordInput())

class CommentForm(forms.Form)
	comment = forms.CharField(widget=forms.TextArea)

class StringsForm(forms.Form)
	firstname = forms.CharField(label='First name', max_length=100)
	lastname = forms.CharField(label='Last name', max_length=100)

class NumbersForm(forms.Form)
	num1 = forms.IntegerField()
	num2 = forms.IntegerField()