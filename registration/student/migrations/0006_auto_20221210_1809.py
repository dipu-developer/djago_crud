# Generated by Django 3.0.5 on 2022-12-10 12:39

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('student', '0005_auto_20221210_1014'),
    ]

    operations = [
        migrations.AlterField(
            model_name='studentreg',
            name='file',
            field=models.FileField(null=True, upload_to='images/'),
        ),
        migrations.AlterField(
            model_name='studentreg',
            name='gender',
            field=models.CharField(choices=[('Male', 'Male'), ('Female', 'Female')], max_length=6),
        ),
        migrations.AlterField(
            model_name='studentreg',
            name='time',
            field=models.DateTimeField(blank=True, default=datetime.datetime(2022, 12, 10, 18, 9, 9, 785098)),
        ),
    ]
