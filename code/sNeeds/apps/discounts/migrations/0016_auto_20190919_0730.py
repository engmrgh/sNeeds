# Generated by Django 2.2.3 on 2019-09-19 07:30

from django.db import migrations
import sNeeds.apps.discounts.models


class Migration(migrations.Migration):
    dependencies = [
        ('discounts', '0015_auto_20190912_1728'),
    ]

    operations = [
        migrations.AlterField(
            model_name='consultantdiscount',
            name='code',
            field=sNeeds.apps.discounts.models.CICharField(max_length=128, unique=True),
        ),
    ]
