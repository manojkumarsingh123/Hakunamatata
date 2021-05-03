import math

from django.db import models

from carts.models import carts
from django.db.models.signals import pre_save, post_save
from decimal import Decimal
import datetime
from datetime import date
from django.conf import settings
from billing.models import BillingProfile
User = settings.AUTH_USER_MODEL
# Create your models here.


class orders(models.Model):
    billing_profile     = models.ForeignKey(BillingProfile, null=True, blank=True)

    #user_address    = models.ForeignKey(Address, related_name="user_address",null=True, blank=True)


    user        = models.OneToOneField(User,null=True, blank=True)
    cart          = models.ForeignKey(carts)

    checkoutdate   = models.DateField(default=date.today)
    total         = models.DecimalField(default=0.00, max_digits=100, decimal_places=2)

    #updated             = models.DateTimeField(auto_now=True)
    #timestamp           = models.DateTimeField(auto_now_add=True)


    def __str__(self):
        return str(self.checkoutdate )
        #here if we write return self.Bookingdate then give below error
#TypeError: __str__ returned non-string (type Bookingdate)
# to resolve this issue we return link this return str(self.Bookingdate )
    def update_total(self):
        cart_total = self.cart.total

        new_total = cart_total

        self.total = new_total
        self.save()
        return new_total



def post_save_cart_total(sender, instance, created, *args, **kwargs):
    if not created:
        cart_obj = instance
        cart_total = cart_obj.total
        cart_id = cart_obj.id
        qs = orders.objects.filter(cart__id=cart_id)
        if qs.count() == 1:
            order_obj = qs.first()
            order_obj.update_total()

post_save.connect(post_save_cart_total, sender=carts)


def post_save_order(sender, instance, created, *args, **kwargs):
    #print("running")
    if created:

        instance.update_total()


post_save.connect(post_save_order, sender=orders)
