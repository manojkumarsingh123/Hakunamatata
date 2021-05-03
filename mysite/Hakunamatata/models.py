from django.db import models
from django.contrib.auth.models import User #user is here from user model which have alredy username,email id.password section
from datetime import date

# Create your models here.

class contactform(models.Model):
    first_name = models.CharField(max_length=128)
    last_name  = models.CharField(max_length=128)
    email      = models.EmailField(max_length=254,unique=True)
    message    = models.TextField(max_length=500,blank=True)


class UserProfileInfo(models.Model):

    # Create relationship (don't inherit from User!)
   user = models.OneToOneField(User)
#user = models.OneToOneField(User) means that in model class user here add more section which dont have user model
#user model have only username,email id.password classes and with the help of one to one from profile info class added


   dob =models.DateField(default=date.today)
    # Add any additional attributes you want
   #not compulsary to upload image
    # Optional: pip install pillow --global-option=”build_ext” --global-option=”--disable-jpeg”
   profile_pic = models.ImageField(upload_to='profile_pics',blank=True)
    #after fill info and uploading img img automatically store in to the media  folder inside project
   def __str__(self):
        # Built-in attribute of django.contrib.auth.models.User !
        return self.user.username # username is default attribute of user
