# Generated by Django 2.2.3 on 2019-07-11 18:03

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('account', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='TimeSlotSale',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('start_time', models.DateTimeField()),
                ('end_time', models.DateTimeField()),
                ('price', models.IntegerField()),
                ('consultant', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='time_slot_sales', to='account.ConsultantProfile')),
            ],
        ),
    ]