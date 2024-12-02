from django.db import models
import math
from django.core.validators import MaxValueValidator, MinValueValidator

# Create your models here.

SEX_CHOICES=[("Male", "Male"),
             ("Female", "Female")]

MARTIAL_STATUS= [("Married","Married"),
                 ("Unmarried", "Unmarried")]

LOAN_TENURE = [(10, 10),
               (15, 15)]

class ClientDetails(models.Model):
    name = models.CharField(max_length=100, default='Ram Rai')
    sex=models.CharField(max_length=8, choices=SEX_CHOICES, default="Male")
    martial= models.CharField(max_length=20, choices=MARTIAL_STATUS, default= "Married")
    age = models.PositiveIntegerField(default= 30)
    salary= models.FloatField(blank=True, default=0.0)
    family_income= models.FloatField(blank=True, default= 0.0)
    home_value = models.FloatField(blank= True, default=571430)
    loan_amount = models.PositiveIntegerField(validators=[
            MinValueValidator(400000),
            MaxValueValidator(15000000)
        ], default= 400000)
    tenure= models.PositiveIntegerField(choices=LOAN_TENURE, default= 15)
    interest= models.FloatField(default = 9.41)
    

    
    
    def __str__(self):
        return self.name 
    
   