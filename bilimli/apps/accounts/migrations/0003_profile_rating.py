# Generated by Django 3.0.7 on 2020-08-02 14:42

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0002_auto_20200802_1206'),
    ]

    operations = [
        migrations.AddField(
            model_name='profile',
            name='rating',
            field=models.IntegerField(default=0, verbose_name='Rating'),
        ),
    ]
