# Generated by Django 2.2.3 on 2019-07-26 07:56

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('account', '0015_auto_20190726_0754'),
    ]

    operations = [
        migrations.AlterField(
            model_name='consultantprofile',
            name='resume',
            field=models.FileField(null=True, upload_to='account/resume/'),
        ),
    ]
