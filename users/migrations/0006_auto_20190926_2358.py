# Generated by Django 2.2.5 on 2019-09-26 17:58

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0005_remove_post_gender'),
    ]

    operations = [
        migrations.AlterField(
            model_name='post',
            name='posteddatetime',
            field=models.DateTimeField(default=datetime.datetime(2019, 9, 26, 23, 58, 11, 275533)),
        ),
    ]