# Generated by Django 3.2.12 on 2022-05-09 05:33

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0005_vendor_is_activated'),
    ]

    operations = [
        migrations.AlterField(
            model_name='customer',
            name='customuser',
            field=models.OneToOneField(blank=True, on_delete=django.db.models.deletion.CASCADE, primary_key=True, serialize=False, to=settings.AUTH_USER_MODEL),
        ),
    ]
