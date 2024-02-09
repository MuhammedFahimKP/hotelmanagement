from django.db import models

# Create your models here.
from accounts.models import MyUser 
from bookings.models import Bookings
from BaseModels.models import BaseModel





CHECK_IN_STATUS = [
    
    ('CheckedIn','CheckedIn'),
    ('CheckedOut','CheckedOut'),
]




class CheckIn(models.Model):
    booking      = models.ForeignKey(Bookings,on_delete=models.CASCADE)
    check_in_at  = models.DateTimeField()
    check_out_at = models.DateTimeField(null=True)
    
    def __str__(self):
        return f'{self.booking.user}'
    
    
    
    