# Generated by Django 3.2.12 on 2022-05-09 03:17

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0005_vendor_is_activated'),
        ('store', '0006_order_complete'),
    ]

    operations = [
        migrations.CreateModel(
            name='ShippingAddress',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('address', models.CharField(max_length=250)),
                ('city', models.CharField(max_length=50)),
                ('state', models.CharField(max_length=50)),
                ('customer', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='accounts.customer')),
                ('order', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='store.order')),
            ],
        ),
    ]
