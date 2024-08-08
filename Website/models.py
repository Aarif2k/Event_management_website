from django.db import models

# Create your models here.

class Event(models.Model):
    img=models.ImageField(upload_to="pic")
    name=models.CharField(max_length=50)
    desc=models.CharField(max_length=1050)

    def __str__(self):
        return self.name
    
class Booking(models.Model):
    customer_name=models.CharField(max_length=55)
    customer_phone_number=models.CharField(max_length=12)
    name=models.ForeignKey(Event,on_delete=models.CASCADE)
    booking_date=models.DateField()
    booked_on=models.DateField(auto_now=True)

    def __str__(self):
        return self.customer_name