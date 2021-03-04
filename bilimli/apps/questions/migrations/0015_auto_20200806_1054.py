# Generated by Django 3.0.5 on 2020-08-06 04:54

import datetime
from django.db import migrations, models
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('questions', '0014_auto_20200804_0732'),
    ]

    operations = [
        migrations.AlterField(
            model_name='answer',
            name='pub_date',
            field=models.DateTimeField(default=datetime.datetime(2020, 8, 6, 4, 54, 21, 667369, tzinfo=utc), verbose_name='Comment pubdate'),
        ),
        migrations.AlterField(
            model_name='question',
            name='pub_date',
            field=models.DateTimeField(default=datetime.datetime(2020, 8, 6, 4, 54, 21, 665369, tzinfo=utc), verbose_name='Publiced Date'),
        ),
    ]
