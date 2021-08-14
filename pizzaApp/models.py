from django.db import models


class Customer(models.Model):
    first_name = models.CharField(max_length=150)
    last_name = models.CharField(max_length=150, null=True)
    phone = models.CharField(max_length=30, null=True)

    def __str__(self):
        return self.first_name + self.last_name


class Ingredient(models.Model):
    name = models.CharField(max_length=100)
    description = models.CharField(max_length=500)

    def __str__(self) -> str:
        return self.name


class Pizza(models.Model):
    name = models.CharField(max_length=100)
    description = models.CharField(max_length=500, null=True)
    ingredients = models.ManyToManyField(Ingredient)
    price = models.PositiveIntegerField()
    weight = models.PositiveSmallIntegerField()

    def __str__(self) -> str:
        return self.name


class Order(models.Model):
    STATUS = (
        ('Pending', 'В ожидании'),
        ('Out for delivery', 'Доставляется'),
        ('Delivered', 'Доставлено'),
    )
    date_created = models.DateTimeField(auto_now_add=True, null=True)
    note = models.CharField(max_length=500, null=True)
    customer = models.ForeignKey(Customer, on_delete=models.CASCADE)
    status = models.CharField(max_length=150, choices=STATUS)
    pizzas = models.ManyToManyField(Pizza)

    def __str__(self) -> str:
        return self.customer.first_name + str(self.date_created)
