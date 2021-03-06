# Generated by Django 2.2.3 on 2019-07-22 13:04

from django.db import migrations, models
import django.db.models.deletion
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('account', '0005_consultantprofile_active'),
        ('store', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='soldtimeslotsale',
            name='consultant',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to='account.ConsultantProfile'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='soldtimeslotsale',
            name='end_time',
            field=models.DateTimeField(default=django.utils.timezone.now),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='soldtimeslotsale',
            name='price',
            field=models.IntegerField(default=11),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='soldtimeslotsale',
            name='start_time',
            field=models.DateTimeField(default=django.utils.timezone.now),
            preserve_default=False,
        ),
    ]
