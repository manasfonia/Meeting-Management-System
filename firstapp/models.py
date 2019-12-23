from datetime import timezone
from phonenumber_field.modelfields import PhoneNumberField
from django.db import models
from django.contrib.auth.models import User


class EmployeeInfo(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    designation = models.CharField(max_length=150)
    phone = PhoneNumberField(null=False, blank=False, unique=True)
    office_address = models.CharField(max_length=255)

    def __str__(self):
        return self.designation

class VisitorInfo(models.Model):
    date_time = models.DateTimeField(default=timezone)
    name = models.CharField(max_length=150)
    address = models.CharField(max_length=255)
    phone = models.CharField(max_length=12)
    email_id = models.EmailField()
    checkout = models.DateTimeField()
    time_slot = models.DateTimeField()
