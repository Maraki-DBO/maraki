# Generated by Django 4.2.10 on 2024-03-08 13:59

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion
import uuid


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0009_remove_card_design_remove_card_other_professions_and_more'),
    ]

    operations = [
        migrations.CreateModel(
            name='BackgroundImageTemplate',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255)),
                ('image', models.ImageField(upload_to='card_backgrounds/')),
                ('used_count', models.PositiveIntegerField(default=0)),
            ],
        ),
        migrations.CreateModel(
            name='Card',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(blank=True, max_length=64)),
                ('company', models.CharField(blank=True, max_length=255)),
                ('website', models.URLField(blank=True)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('is_sharable', models.BooleanField(default=True)),
                ('shared_count', models.PositiveIntegerField(default=0)),
            ],
        ),
        migrations.CreateModel(
            name='CardDesign',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('logo', models.ImageField(blank=True, upload_to='card_designs/')),
                ('brand_color', models.CharField(blank=True, max_length=7)),
                ('front_product_image', models.ImageField(blank=True, upload_to='card_designs/')),
                ('motto', models.CharField(blank=True, max_length=255)),
                ('text_color', models.CharField(blank=True, max_length=7)),
                ('font_family', models.CharField(blank=True, max_length=255)),
                ('back_background_template', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='back_designs', to='core.backgroundimagetemplate')),
                ('front_background_template', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='front_designs', to='core.backgroundimagetemplate')),
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
        migrations.CreateModel(
            name='Layout',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255)),
            ],
        ),
        migrations.CreateModel(
            name='Profession',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255, unique=True)),
                ('icon', models.ImageField(blank=True, null=True, upload_to='profession_icons/')),
            ],
        ),
        migrations.CreateModel(
            name='Sharing',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('shared_at', models.DateTimeField(auto_now_add=True)),
                ('unique_identifier', models.UUIDField(default=uuid.uuid4, unique=True)),
                ('card', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='core.card')),
            ],
        ),
        migrations.CreateModel(
            name='SocialLink',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('url', models.URLField(max_length=2000)),
            ],
        ),
        migrations.CreateModel(
            name='SocialPlatform',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50, unique=True)),
                ('icon', models.ImageField(blank=True, null=True, upload_to='social_media_icons/')),
            ],
        ),
        migrations.DeleteModel(
            name='Title',
        ),
        migrations.RemoveField(
            model_name='user',
            name='address',
        ),
        migrations.RemoveField(
            model_name='user',
            name='biography',
        ),
        migrations.RemoveField(
            model_name='user',
            name='card_limit',
        ),
        migrations.RemoveField(
            model_name='user',
            name='cv',
        ),
        migrations.RemoveField(
            model_name='user',
            name='shareable_card_limit',
        ),
        migrations.RemoveField(
            model_name='user',
            name='title',
        ),
        migrations.CreateModel(
            name='CardPopularity',
            fields=[
                ('card', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, primary_key=True, serialize=False, to='core.card')),
                ('total_views', models.PositiveIntegerField(default=0)),
                ('saved_count', models.PositiveIntegerField(default=0)),
            ],
        ),
        migrations.DeleteModel(
            name='Address',
        ),
        migrations.DeleteModel(
            name='EducationLevel',
        ),
        migrations.AddField(
            model_name='sociallink',
            name='platform',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='core.socialplatform'),
        ),
        migrations.AddField(
            model_name='sociallink',
            name='user',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
        ),
        migrations.AddField(
            model_name='sharing',
            name='shared_from',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='shared_from', to=settings.AUTH_USER_MODEL),
        ),
        migrations.AddField(
            model_name='sharing',
            name='shared_to',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='shared_to', to=settings.AUTH_USER_MODEL),
        ),
        migrations.AddField(
            model_name='carddesign',
            name='layout',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='core.layout'),
        ),
        migrations.AddField(
            model_name='card',
            name='design',
            field=models.OneToOneField(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='core.carddesign'),
        ),
        migrations.AddField(
            model_name='card',
            name='other_professions',
            field=models.ManyToManyField(blank=True, related_name='other_professions', to='core.profession'),
        ),
        migrations.AddField(
            model_name='card',
            name='owner',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
        ),
        migrations.AddField(
            model_name='card',
            name='primary_profession',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='primary_professions', to='core.profession'),
        ),
        migrations.AlterUniqueTogether(
            name='sociallink',
            unique_together={('user', 'platform')},
        ),
    ]
