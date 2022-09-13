from django.db import models

class Currency(models.Model):
    name = models.CharField(max_length=32, verbose_name='Валюта')

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'Валюта'
        verbose_name_plural = 'Валюты'

class Item(models.Model):
    name = models.CharField(max_length=255, verbose_name='Название')
    price = models.PositiveIntegerField(verbose_name='Цена')
    description = models.TextField(null=True, blank=True, verbose_name='Описание')
    currency = models.ForeignKey(Currency, on_delete=models.PROTECT, verbose_name='Валюта')

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'Товары'
        verbose_name_plural = 'Товары'

class Order(models.Model):
    number = models.PositiveBigIntegerField(db_index=True)
    item = models.ForeignKey(Item, on_delete=models.CASCADE, related_name='items', verbose_name='Товар')

    def __str__(self):
        return str(self.pk)

    class Meta:
        verbose_name = 'Заказ'
        verbose_name_plural = 'Заказы'

class Discount(models.Model):
    discount = models.PositiveIntegerField(verbose_name='Скидка')
    order = models.ForeignKey(Order, on_delete=models.CASCADE, verbose_name='Заказ')

    def __str__(self):
         return self.pk

    class Meta:
        verbose_name = 'Скидка'
        verbose_name_plural = 'Скидки'
