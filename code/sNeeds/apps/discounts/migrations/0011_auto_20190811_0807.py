# Generated by Django 2.2.3 on 2019-08-11 08:07

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('discounts', '0010_auto_20190809_0410'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='consultantdiscount',
            name='active',
        ),
        migrations.RemoveField(
            model_name='consultantdiscount',
            name='end',
        ),
        migrations.RemoveField(
            model_name='consultantdiscount',
            name='start',
        ),
    ]
