from django.db import models
from django.utils import timezone

from main.models import BaseEnty


class Departament(BaseEnty):
    dep_id = models.CharField(max_length=32, unique=True, verbose_name='Bo\'lim id')
    name = models.CharField(max_length=128, verbose_name='Bo\'lim nomi')
    is_active = models.BooleanField(default=True, verbose_name='Faolligi')

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'Bo\'lim '
        verbose_name_plural = 'Bo\'limlar '
        ordering = ['dep_id']


class Role(BaseEnty):
    name = models.CharField(max_length=100, verbose_name='Lavozim nomi')
    is_active = models.BooleanField(default=True, verbose_name='Faolligi')

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'Lavozim '
        verbose_name_plural = 'Lavozimlar '


class Employee(BaseEnty):
    GENDER = (
        ['ergkak', 'Erkak'],
        ['ayol', 'Ayol']
    )
    full_name = models.CharField(max_length=100, verbose_name='FIO')
    passport = models.CharField(max_length=9, verbose_name='Passport seriya raqam')
    birth_day = models.DateField(verbose_name='Tug\'ilgan sana')
    gender = models.CharField(max_length=6, choices=GENDER, verbose_name='Jinsi')
    address = models.CharField(max_length=200, verbose_name='Manzil')
    hire_date = models.DateField(default=timezone.now, verbose_name='Ishga  qabul qilingan')
    is_active = models.BooleanField(default=True, verbose_name='Faolligi')
    dept = models.ForeignKey(Departament, verbose_name='Bo\'lim', on_delete=models.CASCADE, null=True)
    em_role = models.ForeignKey(Role, verbose_name='Lavozim', related_name='em_role', on_delete=models.CASCADE, null=True)
    image = models.ImageField(upload_to='images/employee/', default='images/employee/employee.png')

    def __str__(self):
        return self.full_name

    class Meta:
        verbose_name = 'Hodim '
        verbose_name_plural = 'Hodimlar '
