# Generated by Django 2.2.3 on 2019-08-13 05:38

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('account', '0026_auto_20190811_1006'),
    ]

    operations = [
        migrations.AlterField(
            model_name='country',
            name='slug',
            field=models.SlugField(help_text='Lowercase pls', unique=True),
        ),
        migrations.AlterField(
            model_name='fieldofstudy',
            name='slug',
            field=models.SlugField(help_text='Lowercase pls', unique=True),
        ),
        migrations.AlterField(
            model_name='university',
            name='slug',
            field=models.SlugField(help_text='Lowercase pls', unique=True),
        ),
    ]
