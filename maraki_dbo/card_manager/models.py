from django.db import models
from django.contrib.auth import get_user_model
from core.models import Profession

import uuid

User = get_user_model()

# Create your models here.
class Layout(models.Model):
    name = models.CharField(max_length=255)  # Descriptive name for the layout

    def __str__(self):
        return self.name

class BackgroundImageTemplate(models.Model):
    name = models.CharField(max_length=255)  # Descriptive name for the template

    # Image file
    image = models.ImageField(upload_to="card_backgrounds/")

    # Usage statistics (optional)
    used_count = models.PositiveIntegerField(default=0)  # Track how many times the template has been used

    def __str__(self):
        return self.name

# Card Design Model
class CardDesign(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    # Logo
    logo = models.ImageField(upload_to="card_designs/", blank=True)

    # Front Side
    brand_color = models.CharField(max_length=7, blank=True)  # Optional brand color for front shape/image (e.g., "#FFFFFF")
    front_product_image = models.ImageField(upload_to="card_designs/", blank=True)  # Optional front product image

    # Background (Front and Back)
    front_background_template = models.ForeignKey(BackgroundImageTemplate, on_delete=models.SET_NULL, null=True, related_name="front_designs")
    back_background_template = models.ForeignKey(BackgroundImageTemplate, on_delete=models.SET_NULL, null=True, related_name="back_designs")

    # Text (Optional)
    motto = models.CharField(max_length=255, blank=True)  # Optional motto text
    text_color = models.CharField(max_length=7, blank=True)  # Color code (e.g., "#FFFFFF")
    font_family = models.CharField(max_length=255, blank=True)  # Font family name

    # Layout (Optional)
    layout = models.ForeignKey(Layout, on_delete=models.SET_NULL, null=True, blank=True, related_name="designs")

    def __str__(self):
        return f"{self.card.owner.username}'s Card Design"


# Card Model
class Card(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    owner = models.ForeignKey(User, on_delete = models.CASCADE)
    name = models.CharField(max_length = 64, blank = True)
    company = models.CharField(max_length=255, blank=True)
    website = models.URLField(blank=True)  # Optional website URL

    primary_profession = models.ForeignKey(Profession, on_delete=models.SET_NULL, null=True, related_name="primary_professions")
    other_professions = models.ManyToManyField(Profession, related_name="other_professions", blank=True)
    
    design = models.OneToOneField(CardDesign, on_delete=models.SET_NULL, null=True, blank=True)  # Optional design details
    created_at = models.DateTimeField(auto_now_add=True)  # Card creation timestamp

    # Sharing
    is_sharable = models.BooleanField(default=True)  # Control shareability
    shared_count = models.PositiveIntegerField(default=0)  # Track total shares

    def __str__(self):
        return f"{self.owner.username}'s Card"  



class CardShare(models.Model):
    card = models.ForeignKey(Card, on_delete=models.CASCADE)
    shared_through = models.CharField(max_length=50, choices=[('email', 'Email'), ('qr_code', 'QR Code'), ('other', 'Other')], default='other')  # Sharing method
    shared_at = models.DateTimeField(auto_now_add=True)  # Timestamp of sharing

class Sharing(models.Model):
    shared_from = models.ForeignKey(User, on_delete=models.CASCADE, related_name="shared_from")
    shared_to = models.ForeignKey(User, on_delete=models.SET_NULL, related_name="shared_to", null=True, blank=True)
    card = models.ForeignKey(Card, on_delete=models.CASCADE)
    shared_at = models.DateTimeField(auto_now_add=True)
    unique_identifier = models.UUIDField(default=uuid.uuid4, unique=True)  # Use UUIDField

    def __str__(self):
        return f"{self.shared_from.username} shared {self.card} with {self.shared_to.username}"
    
class CardPopularity(models.Model):
    card = models.OneToOneField(Card, on_delete=models.CASCADE, primary_key=True)
    total_views = models.PositiveIntegerField(default=0)  # Total views of the card
    saved_count = models.PositiveIntegerField(default=0)  # Number of times the card is saved to contacts

# Social Media Platform Name Model
class SocialPlatform(models.Model):
    name = models.CharField(max_length=50, unique=True)  # Store platform name (e.g., "facebook", "linkedin")
    icon = models.ImageField(upload_to="social_media_icons/", blank=True, null=True)  # Optional icon for the platform

    def __str__(self) -> str:
        return self.name


# Social Media Link Model
class SocialLink(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    platform = models.ForeignKey(SocialPlatform, on_delete=models.CASCADE)  # Reference the Platform model
    url = models.URLField(max_length=2000)  # Store the full URL for the user's profile

    class Meta:
        unique_together = (('user', 'platform'),)  # Enforce unique links per platform for a user