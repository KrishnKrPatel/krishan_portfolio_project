# Generated by Django 4.0.1 on 2024-12-24 21:11

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='contactmessage',
            name='mobile_no',
            field=models.CharField(max_length=50, verbose_name='Mobile Number'),
            preserve_default=False,
        ),
    ]
