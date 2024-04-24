from django.db import models

# Create your models here.
class Helper(models.Model):
    name = models.CharField(max_length=100)
    gender = models.CharField(max_length=10)
    skill = models.CharField(max_length=100)
    age = models.IntegerField()

    def __str__(self):
        return self.name

class Customer(models.Model):
    name = models.CharField(max_length=100)
    address = models.TextField()
    gender = models.CharField(max_length=10)
    age = models.IntegerField()

    def __str__(self):
        return self.name
    
class AssignHelper(models.Model):
    Customer_name = models.CharField(max_length=100)
    Helper_name = models.CharField(max_length=100)
    skill = models.CharField(max_length=100)
    
    

    def __str__(self):
        return self.skill