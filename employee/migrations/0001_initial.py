# Generated by Django 4.1.1 on 2022-09-16 09:42

from django.db import migrations, models
import django.db.models.deletion
import django.utils.timezone


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('main', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Departament',
            fields=[
                ('baseenty_ptr', models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True, serialize=False, to='main.baseenty')),
                ('dep_id', models.CharField(max_length=32, unique=True, verbose_name="Bo'lim id")),
                ('name', models.CharField(max_length=128, verbose_name="Bo'lim nomi")),
                ('is_active', models.BooleanField(default=True, verbose_name='Faolligi')),
            ],
            bases=('main.baseenty',),
        ),
        migrations.CreateModel(
            name='Role',
            fields=[
                ('baseenty_ptr', models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True, serialize=False, to='main.baseenty')),
                ('name', models.CharField(max_length=100, verbose_name='Lavozim nomi')),
                ('is_active', models.BooleanField(default=True, verbose_name='Faolligi')),
            ],
            bases=('main.baseenty',),
        ),
        migrations.CreateModel(
            name='Employee',
            fields=[
                ('baseenty_ptr', models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True, serialize=False, to='main.baseenty')),
                ('full_name', models.CharField(max_length=100, verbose_name='FIO')),
                ('passport', models.CharField(max_length=9, verbose_name='Passport seriya raqam')),
                ('birth_day', models.DateField(verbose_name="Tug'ilgan sana")),
                ('gender', models.CharField(choices=[['ergkak', 'Erkak'], ['ayol', 'Ayol']], max_length=6, verbose_name='Jinsi')),
                ('address', models.CharField(max_length=200, verbose_name='Manzil')),
                ('hire_date', models.DateField(default=django.utils.timezone.now, verbose_name='Ishga  qabul qilingan')),
                ('is_active', models.BooleanField(default=True, verbose_name='Faolligi')),
                ('image', models.ImageField(default='images/employee/employee.png', upload_to='images/employee/')),
                ('dept', models.ManyToManyField(null=True, to='employee.departament', verbose_name="B'lim")),
                ('role', models.ManyToManyField(related_name='em_role', to='employee.role', verbose_name="B'lim")),
            ],
            options={
                'verbose_name': '3. Hodim ',
                'verbose_name_plural': '3. Hodimlar ',
            },
            bases=('main.baseenty',),
        ),
    ]
