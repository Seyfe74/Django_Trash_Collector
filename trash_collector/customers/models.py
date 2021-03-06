from django.db import models




class Customer(models.Model):
    user = models.ForeignKey('accounts.User', blank=True, null=True, on_delete=models.CASCADE)
    name = models.CharField(max_length=50)
    address = models.CharField(max_length=50)
    zip_code = models.CharField(max_length=50)
    balance  = models.CharField(max_length=50)
    one_time_pickup = models.DateField(null = True)
    weekly_pickup_day = models.CharField(max_length=50)
    suspend_start = models.DateField(null = True) 
    suspend_end = models.DateField(null = True)
    suspend_status = models.BooleanField(null = True)
    pickup_status = models.BooleanField(null = True)

    def __str__(self):
        return self.name
