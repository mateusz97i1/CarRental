from django.db import models
from django.core.validators import MaxValueValidator,MinLengthValidator
from django.core.exceptions import ValidationError
from datetime import datetime


  
class CarModel(models.Model):


    car=models.CharField(max_length=25)
    
    def clean(self):
    # Capitalize the name before saving
        self.car = self.car.capitalize()

    def save(self, *args, **kwargs):
        # Capitalize the name before saving
        self.car = self.car.capitalize()
        super().save(*args, **kwargs)

    
    def __str__(self):
        return self.car
                                  


# Create your models here.
class RentCarModel(models.Model):

    fullName=models.CharField(max_length=50)
    country=models.CharField(max_length=50)
    idNumber=models.CharField(max_length=50,null=False)
    phone=models.IntegerField(max_length=9)
    email=models.EmailField()
    carBrand=models.ForeignKey(CarModel, on_delete=models.CASCADE)
    fromDate=models.DateField(max_length=50,default='2023-01-01')
    toDaate=models.DateField(max_length=50,default='2023-01-01')
    otheText=models.TextField(max_length=250,blank=True,null=True)

    def __str__(self):
        return self.fullName
    
class FaqModel(models.Model):

    text=models.TextField(max_length=250,blank=True,null=True)
    email=models.EmailField()


class RateUSModel(models.Model):

    text=models.TextField(max_length=250,blank=True,null=True)
    nick=models.TextField(max_length=250,blank=False,null=False)
    rating=models.CharField(max_length=6,null=False)
    date=models.DateTimeField(default=datetime.now())
