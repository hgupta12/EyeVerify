# Generated by Django 4.0.10 on 2023-09-06 13:43

import content.models
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('content', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='content',
            name='image_url',
            field=models.ImageField(blank=True, null=True, upload_to=content.models.upload_to),
        ),
    ]