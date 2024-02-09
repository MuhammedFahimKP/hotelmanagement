
from django.db import models


from BaseModels.models import BaseModel
from accounts.models import MyUser




# Create your models here.

PAYMENT_MODES = [
    ('PAY_AT_CHEK_IN','PAY_AT_CHEK_IN'),
    ('RazorPay','RazorPay'),
]

BOOKING_STATUS = [   
    ('booked','booked'),
    ('canceled','canceled')
]


PAYMENT_STATUS = [
    ('PAID','PAID'),
    ('PENDING','PENDING'),

]
        
    
class Bookings(BaseModel):
    
    user           = models.ForeignKey(MyUser,on_delete=models.CASCADE,related_name='customer')
    guestes        = models.IntegerField()
    payment_mode   = models.CharField(max_lenght=50,choices=PAYMENT_MODES)
    payment_status = models.CharField(max_lentgh=20,choices=PAYMENT_STATUS)
    transacion_id  = models.CharField(max_length=200,null=True)
    status         = models.CharField(max_length=30,choices=BOOKING_STATUS)
    
    
    def __str__(self):
        return f'{self.pk} {self.user.first_name}'
    
    
    @property
    def delete(self):
        self.status 
    
    
    
    
    

