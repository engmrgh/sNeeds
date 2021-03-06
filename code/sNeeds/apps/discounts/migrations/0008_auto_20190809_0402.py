# Generated by Django 2.2.3 on 2019-08-09 04:02

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('discounts', '0007_auto_20190809_0400'),
    ]

    operations = [
        migrations.AlterField(
            model_name='cartconsultantdiscount',
            name='cart',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='carts.Cart'),
        ),
        migrations.AlterField(
            model_name='cartconsultantdiscount',
            name='consultant_discount',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='discounts.ConsultantDiscount'),
        ),
    ]
