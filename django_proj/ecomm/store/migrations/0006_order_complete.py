# Generated by Django 3.2.12 on 2022-04-14 14:19

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('store', '0005_orderitem_status'),
    ]

    operations = [
        migrations.AddField(
            model_name='order',
            name='complete',
            field=models.BooleanField(default=False, null=True),
        ),
    ]
