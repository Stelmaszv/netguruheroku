from django.db import models
import json

# Create your models here.
class Rate(models.Model):
    id = models.AutoField(primary_key=True)
    rate   = models.IntegerField(null=True)
    car   = models.ForeignKey(to='netgurutask.Car', on_delete=models.CASCADE, related_name='car',null=True)

class Car(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=100)
    model = models.CharField(max_length=100)
    rates_number = models.IntegerField(default=0,null=False)
    avg_rating   = models.FloatField(default=0)
    rates = models.ManyToManyField(to='netgurutask.Rate', related_name='rates')

    def __init__(self, *args, **kwargs):
        super(Car, self).__init__(*args, **kwargs)
        self.set_avrage_reating()

    def save(self, *args, **kwargs):
        json_results=self.get_JSON()
        found=False
        for item in json_results:
            if item['Make_Name'] == self.name:
                found=True
        if found is False:
            raise ValueError("Car doesn't exist !")
        super(Car, self).save(*args, **kwargs)

    def set_avrage_reating(self):
        if self.id is not None:
            rote=0
            for item in self.rates.all():
                rote=rote+item.rate
            if self.rates.count()>0:
                self.avg_rating=rote/self.rates.count()
            else:
                self.avg_rating=0

    def get_JSON(self):
        with open('getallmakes.json') as f:
            data = json.load(f)
        return data['Results']

    def __str__(self):
        return self.name
