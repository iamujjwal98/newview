
from django.db import models
from django.utils import timezone
# Create your models here.

class Bank_hol(models.Model):
    h_type=models.CharField(max_length=10)
    h_name=models.CharField(max_length=10)
    h_date=models.DateField()
    sc_gp=models.CharField(max_length=10)
    def __str__(self):
        return self.h_name  
    


class EX_hol(models.Model):
    h_type=models.CharField(max_length=10)
    h_name=models.CharField(max_length=10)
    h_date=models.DateField()
    sc_gp=models.CharField(max_length=10)
    def __str__(self):
        return self.h_name
    
