from django.contrib import admin
# from django.contrib.auth.admin import UserAdmin
# from django.contrib.auth.forms import UserCreationForm, UserChangeForm
# from .models import User

# Register your models here.
from . import models
from django.apps import apps

models_to_ignore = [  
       'admin.LogEntry',  
       'contenttypes.ContentType',  
       'sessions.Session',  
       'authtoken.TokenProxy',  
       'authtoken.Token',  # We automatically register the authtoken app models.  
   ]  

# admin.site.register(models.User)
# admin.site.register(models.Address)

for model in apps.get_models():
    try: 
        if model._meta.label in models_to_ignore:
            continue
        else:
            class modelAdmin(admin.ModelAdmin):
                list_display = [field.name for field in model._meta.fields]
            
            admin.site.register(model, modelAdmin)
    except admin.sites.AlreadyRegistered:
        pass
