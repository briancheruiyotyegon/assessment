from django.contrib.auth.models import AbstractUser
from django.db import models

class CustomUser(AbstractUser):
    location = models.CharField(max_length=100)
    address = models.CharField(max_length=100)
    phone = models.CharField(max_length=100)
    role = models.CharField(max_length=100)
    REQUIRED_FIELDS = ['location', 'address', 'phone', 'role']
    def __str__(self):
        return self.username
    
class Category(models.Model):
    user = models.ForeignKey(CustomUser, on_delete=models.CASCADE)
    name = models.CharField(max_length=255)
    description = models.TextField(blank=True)
    additional_info = models.TextField(blank=True)
    date_register = models.DateField(auto_now_add=True)

    def __str__(self):
        return self.name
class Data(models.Model):
    user = models.ForeignKey(CustomUser, on_delete=models.CASCADE)
    category = models.ForeignKey(Category, on_delete=models.CASCADE)
    name = models.CharField(max_length=255)
    first_name = models.CharField(max_length=255,null=True, blank=True)
    last_name = models.CharField(max_length=255,null=True, blank=True)
    date_of_birth = models.DateField(null=True, blank=True)
    gender = models.CharField(max_length=10, choices=[('Male', 'Male'), ('Female', 'Female'), ('Other', 'Other')],null=True, blank=True)
    email = models.EmailField(null=True, blank=True)
    phone_number = models.CharField(max_length=20, null=True, blank=True)
    address = models.CharField(max_length=255,null=True, blank=True)
    occupation = models.CharField(max_length=255,null=True, blank=True)
    specialization = models.CharField(max_length=255,null=True, blank=True)
    institution_name = models.CharField(max_length=255,null=True, blank=True)
    institution_type = models.CharField(max_length=255,null=True, blank=True)
    institution_email = models.EmailField(null=True, blank=True)
    institution_phone_number = models.CharField(max_length=20,null=True, blank=True)
    institution_address = models.TextField(null=True, blank=True)
    county= models.CharField(max_length=255,null=True, blank=True)
    specialties = models.TextField(null=True, blank=True)
    facilities = models.TextField(null=True, blank=True)
    operating_hours = models.TextField(null=True, blank=True)
    description = models.TextField(null=True, blank=True)
    eventName=models.CharField(max_length=255,null=True, blank=True)
    eventDescription=models.TextField(null=True, blank=True)
    eventDate=models.DateField(null=True, blank=True)
    eventTime=models.TimeField(null=True, blank=True)
    eventLocation=models.CharField(max_length=255,null=True, blank=True)
    eventDuration=models.CharField(max_length=255,null=True, blank=True)
    eventOrganizer=models.CharField(max_length=255,null=True, blank=True)
    eventOrganizerEmail=models.EmailField(null=True, blank=True)
    eventOrganizerPhone=models.CharField(max_length=255,null=True, blank=True)
    date_register = models.DateField(auto_now_add=True)
    def __str__(self):
        return self.name
