# Generated by Django 2.2.3 on 2019-10-01 18:17

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('account', '0030_auto_20190911_0736'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='consultantprofile',
            name='StudyField',
        ),
        migrations.DeleteModel(
            name='StudyField',
        ),
    ]
