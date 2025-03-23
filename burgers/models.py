from django.db import models

# Create your models here.


class Burger(models.Model):
    name = models.CharField(max_length=20)
    price = models.IntegerField(default=0)
    calories = models.IntegerField(default=0)

    def __str__(self) -> str:
        return str(self.name)

    def __repr__(self) -> str:
        return super().__str__()
