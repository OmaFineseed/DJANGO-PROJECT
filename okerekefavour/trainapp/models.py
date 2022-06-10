from turtle import position
from unicodedata import name
from django.db import models

# Create your models here.
class States(models.Model):
    name= models.CharField(max_length=15)
    capital= models.CharField(max_length=15)
    
    def __str__(self) -> str:
        return self.name
    
class Company(models.Model):
    name= models.CharField(max_length=20)
    age= models.CharField(max_length=3)
    
    def __str__(self) -> str:
            return self.name
       
        
class Company_employee(models.Model):
    name= models.CharField(max_length=25)
    age= models.CharField(max_length=3)
    position= models.CharField(max_length=30)
     
    def __str__(self) -> str:
        return self.name
        
    
    
    
    
    
    

     