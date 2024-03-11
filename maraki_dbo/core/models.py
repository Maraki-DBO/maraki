from django.db import models
from django.contrib.auth import get_user_model

# Create your models here.

User = get_user_model()

# Address Model
class Address(models.Model):
    street_address = models.CharField(max_length = 255)
    city = models.CharField(max_length = 100)
    state_province = models.CharField(max_length = 100, blank=True)
    postal_code = models.CharField(max_length = 20, blank = True)
    country = models.CharField(max_length = 100)

# Title Model
    
class Title(models.Model):
    title = models.CharField(max_length = 12, unique = True)

class EducationLevel(models.Model):
    title = models.CharField(max_length = 255, unique = True)

class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    phone_number = models.CharField(max_length=13, blank=True)
    address = models.ForeignKey(Address, on_delete=models.SET_NULL, blank=True, null=True)
    title = models.ForeignKey(EducationLevel, on_delete=models.SET_NULL, blank=True, null=True)

    biography = models.TextField(max_length=500, blank=True)
    cv = models.FileField(upload_to="cvs/", blank=True)
    
    card_limit = models.PositiveIntegerField(default=100)
    shareable_card_limit = models.PositiveIntegerField(default=50)
    card_type_limit = models.PositiveIntegerField(default=1)
    

    def __str__(self):
        return self.user.username
    

# Profession Model
class Profession(models.Model):
    name = models.CharField(max_length=255, unique=True)
    icon = models.ImageField(upload_to="profession_icons/", blank=True, null=True)


