# Generated by Django 2.2.3 on 2019-08-02 12:42

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('carts', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='cart',
            name='discount_percent',
            field=models.FloatField(default=0),
        ),
    ]
