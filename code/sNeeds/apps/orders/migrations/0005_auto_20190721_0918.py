# Generated by Django 2.2.3 on 2019-07-21 09:18

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('orders', '0004_order_status'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='order',
            name='active',
        ),
        migrations.RemoveField(
            model_name='soldorder',
            name='active',
        ),
    ]