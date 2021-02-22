from django.db import models

# Create your models here.
class Car(models.Model):
    name = models.CharField(max_length=100)
    model = models.CharField(max_length=100)
    rates_number = models.IntegerField(null=True)
    avg_rating   = models.IntegerField(null=True)

    def __str__(self):
        return self.name