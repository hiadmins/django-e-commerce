from django.db import models

# Create your models here.
class Person(models.Model):
    '''
    the model used to store the user information in database
    '''
    userName=models.CharField(max_length=50,unique=True)
    email=models.EmailField(unique=True)
    age=models.IntegerField(default=0)