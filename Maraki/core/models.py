from django.db import models
from django.contrib.auth.models import AbstractUser
from django.contrib.contenttypes.models import ContentType
from django.contrib.contenttypes.fields import GenericForeignKey


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

# User Model
class User(AbstractUser):
    phone_number = models.CharField(max_length = 13, blank = True)
    address = models.ForeignKey(Address, on_delete = models.SET_NULL, blank = True, null = True)
    title = models.ForeignKey(EducationLevel, on_delete = models.SET_NULL, blank = True, null = True )
   

# Profession Model
class Profession(models.Model):
    name = models.CharField(max_length=255, unique=True)

# Card Model
class Card(models.Model):
    owner = models.ForeignKey(User, on_delete = models.CASCADE)
    primary_profession = models.ForeignKey(Profession, on_delete=models.SET_NULL, null=True, related_name="primary_professions")
    other_professions = models.ManyToManyField(Profession, related_name="other_professions", blank=True)
    company = models.CharField(max_length=255, blank=True)

# Card Design Model
class CardDesign(models.Model):
    card = models.OneToOneField(Card, on_delete=models.CASCADE, primary_key=True)
 

# Social Media Platform Name Model
class SocialPlatform(models.Model):
    name = models.CharField(max_length=50, unique=True)  # Store platform name (e.g., "facebook", "linkedin")
    icon = models.ImageField(upload_to="social_media_icons/", blank=True, null=True)  # Optional icon for the platform


# Social Media Link Model
class SocialLink(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    content_type = models.ForeignKey(ContentType, on_delete=models.CASCADE)
    object_id = models.PositiveIntegerField()
    content_object = GenericForeignKey('content_type', 'object_id')
    platform = models.CharField(max_length=50)  # Store platform name (e.g., "facebook", "linkedin")
    url = models.URLField(max_length=2000)  # Store the full URL for the user's profile

    class Meta:
        unique_together = (('user', 'platform'),)  # Enforce unique links per platform for a user

