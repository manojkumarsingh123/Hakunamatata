from django.db import models
from django.db import models
import datetime
from datetime import date
from django.conf import settings # to get  user deetails which is used in model here we must import first settings
from django.db.models.signals import post_save, pre_save
User = settings.AUTH_USER_MODEL
# Create your models here.

class BillingProfile(models.Model):
    user        = models.OneToOneField(User,null=True, blank=True)

    email       = models.EmailField()
    update      = models.DateTimeField(auto_now=True)
    timestamp   = models.DateTimeField(auto_now_add=True)
    def __str__(self):
        return self.email



def user_created_receiver(sender, instance, created, *args, **kwargs):
    if created and instance.email:
        BillingProfile.objects.get_or_create(user=instance, email=instance.email)

post_save.connect(user_created_receiver, sender=User)
