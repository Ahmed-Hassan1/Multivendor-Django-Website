# Generated by Django 3.2.13 on 2022-06-06 10:19

import accounts.models
from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0016_alter_customuser_email'),
    ]

    operations = [
        migrations.AlterModelManagers(
            name='customer',
            managers=[
                ('objects', accounts.models.CustomUserManager()),
            ],
        ),
    ]