# Generated by Django 3.2.12 on 2022-03-27 13:55

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('store', '0005_auto_20220324_1529'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='product',
            name='tag',
        ),
        migrations.AddField(
            model_name='product',
            name='slug',
            field=models.SlugField(max_length=200, null=True),
        ),
    ]
