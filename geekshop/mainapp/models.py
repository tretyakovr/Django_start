from django.db import models


class Category(models.Model):
    name = models.CharField(verbose_name='Наименование', max_length=50, unique=True, blank=False)
    comments = models.TextField(verbose_name='Примечание', blank=True)

    class Meta:
        db_table = 'Category'
        verbose_name = 'Категории товаров'

    def __str__(self):
        return self.name


class Params(models.Model):
    name = models.CharField(verbose_name='Наименование', max_length=50, unique=True, blank=False)
    comments = models.TextField(verbose_name='Примечание', blank=True)

    class Meta:
        db_table = 'Params'
        verbose_name = 'Параметры'

    def __str__(self):
        return self.name


class Products(models.Model):
    name = models.CharField(verbose_name='Наименование', max_length=50, unique=True, blank=False)
    category = models.ForeignKey(Category, on_delete=models.RESTRICT)
    image = models.ImageField(upload_to='product_images', blank=True)
    comments = models.TextField(verbose_name='Примечание', blank=True)

    class Meta:
        db_table = 'Products'
        verbose_name = 'Товары'

    def __str__(self):
        return f'{self.category.name} {self.name}'

class ProdParams(models.Model):
    prod_name = models.ForeignKey(Products, on_delete=models.RESTRICT)
    param_name = models.ForeignKey(Params, on_delete=models.RESTRICT)
    value = models.CharField(verbose_name='Значение параметра', max_length=50, blank=True)
    comments = models.TextField(verbose_name='Примечание', blank=True)

    class Meta:
        db_table = 'ProdParams'
        verbose_name = 'Параметры товара'

    def __str__(self):
        return f'{self.prod_name.name} {self.param_name.name} {self.value}'
