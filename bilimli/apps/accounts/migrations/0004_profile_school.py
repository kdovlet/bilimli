# Generated by Django 3.0.5 on 2020-08-06 04:54

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0003_profile_rating'),
    ]

    operations = [
        migrations.AddField(
            model_name='profile',
            name='school',
            field=models.IntegerField(default=0, verbose_name='School №'),
        ),
    ]
