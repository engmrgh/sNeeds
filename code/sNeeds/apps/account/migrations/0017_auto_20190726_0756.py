# Generated by Django 2.2.3 on 2019-07-26 07:56

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('account', '0016_auto_20190726_0756'),
    ]

    operations = [
        migrations.AlterField(
            model_name='consultantprofile',
            name='profile_picture',
            field=models.ImageField(upload_to='account/consultant_profile_pictures'),
        ),
    ]
