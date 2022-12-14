# Generated by Django 4.1.1 on 2022-09-20 12:49

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('supply', '0004_stock'),
    ]

    operations = [
        migrations.AlterField(
            model_name='stock',
            name='sale',
            field=models.BooleanField(default=True, null=True),
        ),
        migrations.AlterField(
            model_name='stock',
            name='sale_qty',
            field=models.BooleanField(default=True, null=True),
        ),
        migrations.AlterField(
            model_name='stock',
            name='sup_qty',
            field=models.FloatField(default=0, null=True),
        ),
        migrations.AlterField(
            model_name='stock',
            name='supply',
            field=models.ForeignKey(default=0, null=True, on_delete=django.db.models.deletion.CASCADE, to='supply.supplyitem'),
        ),
    ]
