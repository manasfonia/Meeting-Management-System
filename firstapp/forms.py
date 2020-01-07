from django import forms
from django.contrib.auth.models import User
# from bootstrap_datepicker_plus import DateTimePickerInput
from django.urls import reverse
from tempus_dominus.widgets import DatePicker, TimePicker, DateTimePicker
from django.forms import DateTimeInput

from .models import EmployeeInfo, VisitorInfo


class RegistrationForm1(forms.ModelForm):
    class Meta:
        model = User
        fields = ('username', 'first_name', 'last_name', 'email', 'password')
        widgets = {
            'username': forms.TextInput(attrs={'class': 'form-control'}),
            'first_name': forms.TextInput(attrs={'class': 'form-control'}),
            'last_name': forms.TextInput(attrs={'class': 'form-control'}),
            'email': forms.TextInput(attrs={'class': 'form-control'}),
            'password': forms.PasswordInput(attrs={'class': 'form-control'}),
        }


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
                                        'onchange':'getval(this);'}),
            'start_time': forms.TextInput(attrs={'class': 'datetimepicker-input form-control',
                                                  'data-target': '#datetimepicker7' }),
            'end_time': forms.TextInput(attrs={'class': 'datetimepicker-input form-control',
                                                  'data-target': '#datetimepicker8' }),

        }
