# Generated by Django 2.2.3 on 2019-08-09 03:01

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('discounts', '0004_cartconsultantdiscount'),
    ]

    operations = [
        migrations.AlterField(
            model_name='cartconsultantdiscount',
            name='cart',
            field=models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to='carts.Cart'),
        ),
        migrations.RemoveField(
            model_name='cartconsultantdiscount',
            name='consultant_discount',
        ),
        migrations.AddField(
            model_name='cartconsultantdiscount',
            name='consultant_discount',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to='discounts.ConsultantDiscount'),
            preserve_default=False,
        ),
    ]
