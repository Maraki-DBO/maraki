# Generated by Django 4.2.10 on 2024-03-11 22:37

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('card_manager', '0004_card_card_type'),
    ]

    operations = [
        migrations.AlterField(
            model_name='card',
            name='card_type',
            field=models.CharField(blank=True, max_length=50, null=True),
        ),
    ]