from django.db import models
import json

# Create your models here.
class Rate(models.Model):
    id = models.AutoField(primary_key=True)
    rating     = models.IntegerField(null=True)
    car_id     = models.ForeignKey(to='netgurutask.Car', on_delete=models.CASCADE, related_name='car',null=True)

    def save(self, *args, **kwargs):
        if self.rating > 0 and self.rating<6:
            super(Rate, self).save(*args, **kwargs)
            self.car_id.rates.add(self)
        else:
            raise ValueError("Your rate is "+str(self.rating)+"!  Add a rate for a car from 1 to 5 !" )

class Car(models.Model):
    id           = models.AutoField(primary_key=True)
    make         = models.CharField(max_length=100)
    model        = models.CharField(max_length=100)
    rates_number = models.IntegerField(default=1,null=False)
    avg_rating   = models.FloatField(default=1)
    rates = models.ManyToManyField(to='netgurutask.Rate', related_name='rates')

    def __init__(self, *args, **kwargs):

        super(Car, self).__init__(*args, **kwargs)
        self.set_avrage_reating()
        self.set_rates_number()

    def set_rates_number(self):

        if self.id is not None:
            self.rates_number=self.rates.count()

    def delete(self, *args, **kwargs):

        for rate in self.rates.all():
            rate.delete()
        super(Car, self).delete(*args, **kwargs)

    def save(self, *args, **kwargs):

        json_results=self.get_JSON()
        found=False
        for item in json_results:
            if item['Make_Name'] == self.make:
                found=True
        if found is False:
            raise ValueError("Car doesn't exist !")
        super(Car, self).save(*args, **kwargs)

    def set_avrage_reating(self):

        if self.id is not None:
            rote=0
            for item in self.rates.all():
                rote=rote+item.rating
            if self.rates.count()>0:
                self.avg_rating=rote/self.rates.count()

    def get_JSON(self):

        with open('getallmakes.json') as f:
            data = json.load(f)
        return data['Results']

    def __str__(self):
        return self.make
