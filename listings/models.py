from django.db import models
from django.contrib.auth.models import User

# Create your models here.
#these are representations of database schema
#once a model is made we need to add it in admin.py
class Listing(models.Model):
    #columns in the table
    title = models.CharField(max_length=150)
    price = models.IntegerField()
    num_bedrooms = models.IntegerField()
    num_bathrooms = models.IntegerField()
    square_footage = models.IntegerField()
    address = models.CharField(max_length=100)
    image = models.ImageField() #install pillow to work with images
    #change the name of the model listing on display(string representation)
    def __str__(self):
        return self.title


class Profile(models.Model):
    #associate this models with user model
    user = models.OneToOneField(User, null=True, on_delete=models.CASCADE)
    bio = models.TextField()

    def __str__(self): 
        return str(self.user)