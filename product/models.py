from django.db import models
from mptt.models import MPTTModel, TreeForeignKey

from main.models import BaseEnty


class Category(BaseEnty, MPTTModel):
    name = models.CharField(max_length=128, verbose_name="Nomi")
    slug = models.SlugField(max_length=128)
    description = models.TextField(verbose_name='Tavsif')
    is_active = models.BooleanField(default=True, verbose_name="Faolmi")
    parent = TreeForeignKey(
        'self',
        blank=True,
        null=True,
        related_name='child',
        on_delete=models.CASCADE,
        verbose_name='Ajdod'
    )

    class Meta:
        verbose_name = 'Kategoriya '
        verbose_name_plural = 'Kategoriyalar '

    def __str__(self):
        full_path = [self.name]
        k = self.parent
        while k is not None:
            full_path.append(k.name)
            k = k.parent

        return ' -> '.join(full_path[::-1])


class Product(BaseEnty):
    UNITS = [
        ('dona', 'Dona'),
        ('kg', 'Kg'),
    ]

    code = models.IntegerField(verbose_name='Kod')
    category_field = models.ForeignKey(Category, on_delete=models.CASCADE, related_name='products',
                                       verbose_name='Kategoriya')
    title = models.CharField(max_length=128, verbose_name='Nomi')
    description = models.TextField(verbose_name='Tavsif')
    units = models.CharField(verbose_name='Birlik', choices=UNITS, max_length=50)
    is_active = models.BooleanField(default=True, verbose_name='Faolmi')
    slug = models.SlugField(max_length=128)
    image = models.ImageField(upload_to='images/product/', default='images/product/default.png')

    class Meta:
        verbose_name = 'Maxsulot '
        verbose_name_plural = 'Maxsulotlar '
        ordering = ['-created_at']

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return self.slug
