# Generated by Django 2.2.5 on 2019-09-28 08:54

import datetime
from django.db import migrations, models
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0008_auto_20190928_1451'),
    ]

    operations = [
        migrations.AlterField(
            model_name='post',
            name='patientdisease',
            field=models.CharField(default='Patient Diease', max_length=200),
        ),
        migrations.AlterField(
            model_name='post',
            name='posteddatetime',
            field=models.DateTimeField(default=datetime.datetime(2019, 9, 28, 14, 54, 10, 610510, tzinfo=utc)),
        ),
    ]
