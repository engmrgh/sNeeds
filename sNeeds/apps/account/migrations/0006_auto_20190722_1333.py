# Generated by Django 2.2.3 on 2019-07-22 13:33

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('account', '0005_consultantprofile_active'),
    ]

    operations = [
        migrations.AddField(
            model_name='consultantprofile',
            name='profile_picture',
            field=models.ImageField(null=True, upload_to='consultant_profile_pictures'),
        ),
        migrations.AddField(
            model_name='country',
            name='picture',
            field=models.ImageField(null=True, upload_to='country_pictures'),
        ),
        migrations.AddField(
            model_name='fieldofstudy',
            name='picture',
            field=models.ImageField(null=True, upload_to='field_of_study_pictures'),
        ),
        migrations.AddField(
            model_name='university',
            name='picture',
            field=models.ImageField(null=True, upload_to='university_pictures'),
        ),
    ]
