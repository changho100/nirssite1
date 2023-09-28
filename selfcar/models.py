from django.db import models

    
class ReserveSelfcar(models.Model):
    name = models.CharField(max_length=50)
    email = models.CharField(max_length=50)
    reserv_day = models.IntegerField()
    reserv_time = models.IntegerField()
    pub_date = models.DateTimeField('Create Date', auto_now=True)
        
    def __str__(self):
        return self.name