# Generated by Django 4.2.10 on 2024-03-11 17:50

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('authentication', '0005_profile'),
    ]

    operations = [
        migrations.AddField(
            model_name='profile',
            name='phone_number',
            field=models.CharField(default=django.utils.timezone.now, max_length=13),
            preserve_default=False,
        ),
    ]