# Generated by Django 2.2.3 on 2019-07-23 15:29

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('store', '0002_auto_20190722_1304'),
        ('comments', '0005_soldtimeslotstar'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='SoldTimeSlotStar',
            new_name='SoldTimeSlotRate',
        ),
    ]
