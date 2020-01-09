from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from django.forms import DateTimeInput

from .models import EmployeeInfo, VisitorInfo


class RegistrationForm1(UserCreationForm):
    # password1 = forms.CharField(label="Password1", widget=forms.PasswordInput(attrs={'class':'form-control'}))
    # password2 = forms.CharField(label="Password2", widget=forms.PasswordInput(attrs={'class':'form-control'}))
    class Meta:
        model = User
        fields = ('username', 'first_name', 'last_name', 'email', 'password1', 'password2')
        widgets = {
            'username': forms.TextInput(attrs={'class': 'form-control'}),
            'first_name': forms.TextInput(attrs={'class': 'form-control'}),
            'last_name': forms.TextInput(attrs={'class': 'form-control'}),
            'email': forms.TextInput(attrs={'class': 'form-control'}),
            'password1': forms.PasswordInput(attrs={'class': 'form-control'}),
            'password2': forms.PasswordInput(attrs={'class': 'form-control'}),
        }

        def save(self, commit=True):
            user = super(RegistrationForm1, self).save(commit=False)
            user.first_name = self.cleaned_data['first_name']
            user.last_name = self.cleaned_data['last_name']
            user.email = self.cleaned_data['email']

            if commit:
                user.save()

            return user


class RegistrationForm0(forms.ModelForm):
    class Meta:
        model = User
        fields = ('first_name', 'last_name', 'email')
        widgets = {

            'first_name': forms.TextInput(attrs={'class': 'form-control'}),
            'last_name': forms.TextInput(attrs={'class': 'form-control'}),
            'email': forms.TextInput(attrs={'class': 'form-control'}),

        }


class RegistrationForm2(forms.ModelForm):
    class Meta:
        model = EmployeeInfo
        fields = ('designation', 'phone', 'office_address')
        widgets = {
            'designation': forms.TextInput(attrs={'class': 'form-control'}),
            'phone': forms.TextInput(attrs={'class': 'form-control'}),
            'office_address': forms.TextInput(attrs={'class': 'form-control'}),
        }


class VisitorForm(forms.ModelForm):
    class Meta:
        model = VisitorInfo
        fields = ('name', 'address', 'phone', 'email', 'host', 'start_time', 'end_time')

        widgets = {
            'name': forms.TextInput(attrs={'class': 'form-control'}),
            'address': forms.TextInput(attrs={'class': 'form-control'}),
            'phone': forms.TextInput(attrs={'class': 'form-control'}),
            'email': forms.TextInput(attrs={'class': 'form-control'}),
            'host': forms.Select(attrs={'class': 'form-control',
                                        'onchange': 'getval(this);'}),
            'start_time': forms.DateTimeInput(attrs={'class': 'form-control'}),
            'end_time':forms.DateTimeInput(attrs={'class': 'form-control'}),

        }
