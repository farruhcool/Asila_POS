# Generated by Django 4.1.1 on 2022-09-20 04:46

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('supply', '0002_alter_supplier_options_alter_supplybill_options_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='supplyitem',
            name='total_price',
            field=models.IntegerField(default=0, editable=False),
        ),
    ]
