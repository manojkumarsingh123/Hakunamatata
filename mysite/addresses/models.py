from django.db import models
from billing.models import BillingProfile
# Create your models here.
class Address(models.Model):
    billing_profile = models.ForeignKey(BillingProfile)
    name            = models.CharField(max_length=120, null=True, blank=True)
    city            = models.CharField(max_length=120)
    area            = models.CharField(max_length=120)
    pincode         = models.CharField(null=True,max_length=120)
    address         = models.CharField(max_length=120)
    mobile_num      = models.CharField(null=True,max_length=11)

    def __str__(self):
        return str(self.billing_profile)
