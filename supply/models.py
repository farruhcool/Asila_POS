from django.db import models

from main.models import BaseEnty
from product.models import Product


class Supplier(BaseEnty):
    name = models.CharField(max_length=150)
    phone = models.CharField(max_length=20, unique=True)
    address = models.CharField(max_length=200)
    email = models.EmailField(max_length=254, unique=True)
    stir = models.IntegerField(unique=True)
    is_active = models.BooleanField(default=True)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'Ta\'minotchi'
        verbose_name_plural = 'Ta\'minotchilar'


class SupplyBill(BaseEnty):
    bill_no = models.AutoField(primary_key=True)
    time = models.DateTimeField(auto_now=True)
    sup_supplier = models.ForeignKey(Supplier, on_delete=models.CASCADE, related_name='supply_supplier')

    def __str__(self):
        return "Chek №: " + str(self.bill_no)

    def get_items_list(self):
        return SupplyItem.objects.filter(bill_no=self)

    def get_total_price(self):
        purchase_items = SupplyItem.objects.filter(bill_no=self)
        total = 0
        for item in purchase_items:
            total += item.total_price
        return total

    get_total_price.short_description = 'Jami kirim summasi'

    class Meta:
        verbose_name = 'Kirim'
        verbose_name_plural = 'Kirimlar'
        ordering = ['-bill_no']


class SupplyItem(BaseEnty):
    bill_no = models.ForeignKey(SupplyBill, on_delete=models.CASCADE)
    sup_product = models.ForeignKey(Product, on_delete=models.CASCADE, related_name='supply_product')
    quantity = models.IntegerField(default=1)
    per_price = models.IntegerField(default=1)
    total_price = models.IntegerField(editable=False, default=0)

    def __str__(self):
        return "Chek №: " + str(self.bill_no.bill_no) + " | Maxsulot : " + self.sup_product.title

    def save(self, *args, **kwargs):
        self.total_price = self.quantity * self.per_price
        super(SupplyItem, self).save(*args, **kwargs)

        # Stock part
        stock = Stock.objects.filter(product=self.sup_product).order_by('id').first()
        if stock:
            totalBal = stock.total_bal_qty + self.quantity
        else:
            totalBal = self.quantity

        Stock.objects.create(
            product=self.sup_product,
            supply=self,
            sale=None,
            sup_qty=self.quantity,
            sale_qty=None,
            total_bal_qty=totalBal
        )

    class Meta:
        verbose_name = 'Kirim maxsuloti'
        verbose_name_plural = 'Kirim maxsulotlari'
        ordering = ['-id']


class Stock(models.Model):
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    supply = models.ForeignKey(SupplyItem, on_delete=models.CASCADE, default=0, null=True)
    sale = models.BooleanField(default=True, null=True)
    sup_qty = models.FloatField(default=0, null=True)
    sale_qty = models.BooleanField(default=True, null=True)
    total_bal_qty = models.FloatField()

    class Meta:
        verbose_name = 'Ombor '
        verbose_name_plural = 'Omborlar '

    def __str__(self):
        return self.product.title
