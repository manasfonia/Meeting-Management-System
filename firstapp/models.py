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
        return self.user.get_full_name()

class VisitorInfo(models.Model):
    name = models.CharField(max_length=150)
    address = models.CharField(max_length=255)
    phone = PhoneNumberField(null=False, blank=False)
    email = models.EmailField()
    host = models.ForeignKey(EmployeeInfo, on_delete=models.CASCADE)
    timestamp = models.DateTimeField(auto_now_add=True, blank=False)
    checkout = models.DateTimeField(blank=True, null=True)
    start_time = models.DateTimeField(blank=False)
    end_time = models.DateTimeField(blank=False)

    def __str__(self):
        return self.name

    def publish(self):
        self.date_time = timezone.now()
        self.save()

