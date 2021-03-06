# Generated by Django 2.2.3 on 2019-07-22 13:34

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('account', '0007_auto_20190722_1333'),
    ]

    operations = [
        migrations.AlterField(
            model_name='country',
            name='picture',
            field=models.ImageField(upload_to='country_pictures'),
        ),
        migrations.AlterField(
            model_name='fieldofstudy',
            name='picture',
            field=models.ImageField(upload_to='field_of_study_pictures'),
        ),
        migrations.AlterField(
            model_name='university',
            name='picture',
            field=models.ImageField(upload_to='university_pictures'),
        ),
    ]
