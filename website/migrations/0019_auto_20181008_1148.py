# Generated by Django 2.0.5 on 2018-10-08 07:18

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('website', '0018_auto_20181007_2315'),
    ]

    operations = [
        migrations.AddField(
            model_name='bookletfield',
            name='slug',
            field=models.SlugField(null=True),
        ),
        migrations.AddField(
            model_name='booklettopic',
            name='slug',
            field=models.SlugField(null=True),
        ),
    ]
