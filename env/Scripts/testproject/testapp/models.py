from django.contrib.auth.models import User
from django.db import models

# class User(AbstractUser):
#     STATUS_CHOICES = [
#         ('rider', 'Rider'),
#         ('driver', 'Driver'),
#     ]
#     name = models.CharField(max_length=255)
#     phone_number = models.CharField(max_length=13, unique=True)
#     password = models.CharField(max_length=255)
#     typeofuser = models.CharField(max_length=255, choices=STATUS_CHOICES, default='started')
#     USERNAME_FIELD = 'phone_number'
#     REQUIRED_FIELDS = []

class Subzone(models.Model): # dividing the location into zone for finding nearest driver
    id = models.AutoField(primary_key=True)
    zonename = models.CharField(max_length=255)
    pincode=models.BigIntegerField()
    def __str__(self):
        return self.pincode

class Driver(models.Model):
    id = models.BigIntegerField(primary_key=True)
    name = models.CharField(max_length=255)
    status = models.BooleanField(default=True)  # True for available,False for unavailable

    def __str__(self):
        return self.name
    
class Ride(models.Model):
    STATUS_CHOICES = [
        ('started', 'Started'),
        ('completed', 'Completed'),
        ('canceled', 'Canceled'),
    ]
    id = models.AutoField(primary_key=True)
    rider = models.ForeignKey(User, on_delete=models.CASCADE)
    driver = models.ForeignKey(Driver, on_delete=models.CASCADE)
    pickup_location = models.CharField(max_length=255)
    dropoff_location = models.CharField(max_length=255)
    status = models.CharField(max_length=255, choices=STATUS_CHOICES, default='started')
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f"Ride {self.id} ({self.status})"

