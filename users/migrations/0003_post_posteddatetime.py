# Generated by Django 2.2.5 on 2019-09-14 19:45

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0002_auto_20190915_0133'),
    ]

    operations = [
        migrations.AddField(
            model_name='post',
            name='posteddatetime',
            field=models.DateTimeField(default=django.utils.timezone.now),
        ),
    ]