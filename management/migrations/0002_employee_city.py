# Generated by Django 2.0.6 on 2018-06-24 06:06

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('management', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='employee',
            name='city',
            field=models.CharField(default='Hamburg', max_length=30),
        ),
    ]
