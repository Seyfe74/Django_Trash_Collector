from django.db import models
from django.db.models.fields import BooleanField, NullBooleanField
from django.db.models.fields.related import ForeignKey
# Create your models here.

# TODO: Finish customer model by adding necessary operties to fulfill user stories


class Customer(models.Model):
    user =  models.ForeignKey('accounts.User', blank=True, null=True, on_delete=models.CASCADE)
    name = models.CharField(max_length=50)
    address = models.CharField(max_length=50)
    zip_code = models.CharField(max_length=50)
    balance  = models.CharField(max_length=50)
    one_time_pickup = models.DateField(null = True)
    weekly_pickup_day = models.CharField(max_length=50)
    suspend_start = models.DateField(null = True) 
    suspend_end = models.DateField(null = False)
    suspend_status = models.BooleanField()
    pickup_status = models.BooleanField()
