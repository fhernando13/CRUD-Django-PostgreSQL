from django.db import models

# Create your models here.
class Address(models.Model):
    street = models.CharField(max_length=100)
    num = models.IntegerField()
    country = models.CharField(max_length=100)

    def __str__(self):
        return f'Address: {self.id}: {self.street} {self.num} {self.country}'


class User(models.Model):
    name = models.CharField(max_length=100)
    app = models.CharField(max_length=100)
    email = models.CharField(max_length=100)
    address = models.ForeignKey(Address, on_delete=models.SET_NULL, null=True)

    def __str__(self):
        return f'Usuario: {self.id} {self.name} {self.app} {self.email}'

