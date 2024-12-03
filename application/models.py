from django.db import models

# Create your models here.
class Reservation(models.Model):
    name = models.CharField(max_length=20)
    email = models.EmailField(max_length=25)
    phone_number = models.CharField(max_length=20)
    number_of_guests = models.IntegerField()
    reservation_date = models.DateField()
    reservation_time = models.TimeField()
    special_request = models.TextField(blank=True, null=True)



    def __str__(self):
        return self.name