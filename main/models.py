from django.db import models

class CreateBouquet(models.Model):
    customer_name = models.CharField(max_length=30)
    receiver_name = models.CharField(max_length=30)
    order_time = models.DateTimeField(auto_now_add=True)
    size = models.ForeignKey('Size', on_delete=models.PROTECT, null=True)
    flower = models.ForeignKey('Flower', on_delete=models.PROTECT, null=True)
    package = models.ForeignKey('Package', on_delete=models.PROTECT, null=True)
    ribbon = models.ForeignKey('Ribbon', on_delete=models.PROTECT, null=True)

    def __str__(self):
        return f'Заказчик: {self.customer_name}, время: {self.order_time}'

class Size(models.Model):
    name = models.CharField(max_length=30, db_index=True)

    def __str__(self):
        return self.name


class Flower(models.Model):
    name = models.CharField(max_length=30, db_index=True)

    def __str__(self):
        return self.name


class Package(models.Model):
    name = models.CharField(max_length=30, db_index=True)

    def __str__(self):
        return self.name

class Ribbon(models.Model):
    name = models.CharField(max_length=30, db_index=True)

    def __str__(self):
        return self.name