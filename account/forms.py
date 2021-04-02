from django import forms
from django.contrib.auth.models import User


class RegistrationForm(forms.ModelForm):
    password = forms.CharField(min_length=6, required=True, widget=forms.PasswordInput)
    password_confirmation = forms.CharField(min_length=6, required=True, widget=forms.PasswordInput)

    class Meta:
        model = User
        fields = ['username', 'password', 'password_confirmation', 'email', 'first_name', 'last_name']

    def clean_username(self):
        username = self.cleaned_data['username']
        if User.objects.filter(username=username).exists():
            raise forms.ValidationError('Username already exists')
        else:
            return username
    # def clean_email(self):
    #     email = self.cleaned_data['email']
    #     if

    def clean(self):
        data = self.cleaned_data
        password = data.get['password']
        password_confirmation = data.pop('password_confirmation')
        if password != password_confirmation:
            raise forms.ValidationError('Passwords do not match')
        else:
            return data
    def save(self, commit=True):
        user = User.objects.create_user()
        return user

