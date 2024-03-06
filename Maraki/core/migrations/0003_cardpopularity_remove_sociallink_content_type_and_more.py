# Generated by Django 4.2.10 on 2024-03-05 06:31

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion
import uuid


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0002_card_educationlevel_profession_socialplatform_title_and_more'),
    ]

    operations = [
        migrations.CreateModel(
            name='CardPopularity',
            fields=[
                ('card', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, primary_key=True, serialize=False, to='core.card')),
                ('total_views', models.PositiveIntegerField(default=0)),
                ('saved_count', models.PositiveIntegerField(default=0)),
            ],
        ),
        migrations.RemoveField(
            model_name='sociallink',
            name='content_type',
        ),
        migrations.RemoveField(
            model_name='sociallink',
            name='object_id',
        ),
        migrations.AddField(
            model_name='card',
            name='is_sharable',
            field=models.BooleanField(default=True),
        ),
        migrations.AddField(
            model_name='card',
            name='name',
            field=models.CharField(blank=True, max_length=64),
        ),
        migrations.AddField(
            model_name='card',
            name='shared_count',
            field=models.PositiveIntegerField(default=0),
        ),
        migrations.AddField(
            model_name='profession',
            name='icon',
            field=models.ImageField(blank=True, null=True, upload_to='profession_icons/'),
        ),
        migrations.AddField(
            model_name='user',
            name='card_limit',
            field=models.PositiveIntegerField(default=100),
        ),
        migrations.AddField(
            model_name='user',
            name='shareable_card_limit',
            field=models.PositiveIntegerField(default=50),
        ),
        migrations.AlterField(
            model_name='sociallink',
            name='platform',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='core.socialplatform'),
        ),
        migrations.CreateModel(
            name='Sharing',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('shared_at', models.DateTimeField(auto_now_add=True)),
                ('unique_identifier', models.UUIDField(default=uuid.uuid4, unique=True)),
                ('card', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='core.card')),
                ('shared_from', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='shared_from', to=settings.AUTH_USER_MODEL)),
                ('shared_to', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='shared_to', to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='CardShare',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('shared_through', models.CharField(choices=[('email', 'Email'), ('qr_code', 'QR Code'), ('other', 'Other')], default='other', max_length=50)),
                ('shared_at', models.DateTimeField(auto_now_add=True)),
                ('card', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='core.card')),
            ],
        ),
    ]
