# Generated by Django 5.0.4 on 2024-05-08 06:07

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('vendors', '0002_purchaseorder'),
    ]

    operations = [
        migrations.DeleteModel(
            name='PurchaseOrder',
        ),
    ]