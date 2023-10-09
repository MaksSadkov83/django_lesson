from django.db import models


class ProductCategory(models.Model):
    name = models.CharField(max_length=128, unique=True)
    description = models.TextField(null=True, blank=True)

    def __str__(self):
        return self.name


class Product(models.Model):
    name = models.CharField(max_length=256)
    price = models.DecimalField(max_digits=10, decimal_places=3)
    description = models.TextField()
    image = models.ImageField(upload_to='upload_image')
    quantity = models.PositiveIntegerField(default=0)
    category = models.ForeignKey(to=ProductCategory, on_delete=models.PROTECT)

    def __str__(self):
        return f"Продукция: {self.name} | Категория: {self.category}"
