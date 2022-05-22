# Generated by Django 3.2.12 on 2022-05-17 10:58

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('store', '0010_alter_shippingaddress_customer'),
    ]

    operations = [
        migrations.AddField(
            model_name='orderitem',
            name='price',
            field=models.FloatField(default=1),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='orderitem',
            name='quantity',
            field=models.IntegerField(default=0),
        ),
    ]