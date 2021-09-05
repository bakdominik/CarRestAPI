from django.db import models

# Create your models here.

class Car(models.Model):

    make = models.CharField(max_length=50)
    model = models.CharField(max_length=50)

    def __str__(self):
        return "%s %s" % (self.make, self.model)
        

class Rate(models.Model):
    car_id = models.ForeignKey(Car, on_delete=models.CASCADE)
    rating = models.IntegerField(choices=list(zip(range(1, 6), range(1, 6))))
    