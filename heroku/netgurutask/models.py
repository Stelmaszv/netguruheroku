from django.db import models
import json

# Create your models here.
class Car(models.Model):
    name = models.CharField(max_length=100)
    model = models.CharField(max_length=100)
    rates_number = models.IntegerField(null=True)
    avg_rating   = models.IntegerField(null=True)

    def save(self, *args, **kwargs):
        json_results=self.get_JSON()
        found=False
        for item in json_results:
            if item['Make_Name'] == self.name:
                found=True
        if found is False:
            raise ValueError("Car doesn't exist !")
        self.avg_rating=self.set_avrage_reating()
        super(Car, self).save(*args, **kwargs)

    def set_avrage_reating(self):
        return 13

    def get_JSON(self):
        data = ' '
        with open('getallmakes.json') as f:
            data = json.load(f)
        return data['Results']

    def __str__(self):
        return self.name