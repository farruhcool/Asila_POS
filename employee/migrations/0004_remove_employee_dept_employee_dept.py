# Generated by Django 4.1.1 on 2022-09-16 12:24

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('employee', '0003_alter_departament_options_alter_employee_options_and_more'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='employee',
            name='dept',
        ),
        migrations.AddField(
            model_name='employee',
            name='dept',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='employee.departament', verbose_name="Bo'lim"),
        ),
    ]
