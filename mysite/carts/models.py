from decimal import Decimal
from django.db import models
from django.conf import settings
from django.db.models.signals import pre_save, post_save, m2m_changed # this is connected to     services    = models.ManyToManyField(services, blank=True)
#for m2m changed see more on django documentation

# Create your models here.
from services.models import services
User = settings.AUTH_USER_MODEL #comes from settings INSTALLED_APPS = [django.contrib.auth',]


class CartManager(models.Manager):
    def new_or_get(self, request):
        cart_id = request.session.get("cart_id", None)
        qs = self.get_queryset().filter(id=cart_id)
        if qs.count() == 1:
            new_obj = False
            cart_obj = qs.first()
            if request.user.is_authenticated() and cart_obj.user is None:
                cart_obj.user = request.user
                cart_obj.save()
        else:
            cart_obj = carts.objects.new(user=request.user)
            new_obj = True
            request.session['cart_id'] = cart_obj.id
        return cart_obj, new_obj

    def new(self, user=None):
        user_obj = None
        if user is not None:
            if user.is_authenticated():
                user_obj = user
        return self.model.objects.create(user=user_obj)












class carts(models.Model):
    user        = models.ForeignKey(User, null=True, blank=True) # any user create cart
    services    = models.ManyToManyField(services, blank=True)
    subtotal    = models.DecimalField(default=0.00, max_digits=100, decimal_places=2)
    total       = models.DecimalField(default=0.00, max_digits=100, decimal_places=2)

    updated     = models.DateTimeField(auto_now=True)#give time of recentaly updated cart item
    timestamp   = models.DateTimeField(auto_now_add=True) # give info when the cart is created


    objects = CartManager()


    def __str__(self):
        return str(self.id)


def m2m_changed_cart_receiver(sender, instance, action, *args, **kwargs):
    if action == 'post_add' or action == 'post_remove' or action == 'post_clear':
        services = instance.services.all()
        total = 0
        for x in services:
            total += x.price

        instance.subtotal = total
        instance.save()


m2m_changed.connect(m2m_changed_cart_receiver, sender=carts.services.through)




def pre_save_cart_receiver(sender, instance, *args, **kwargs):
    if instance.subtotal > 0:
        instance.total = Decimal(instance.subtotal) * Decimal(1.00) # Ex : here if you want some disscout or tax or extra fee8% tax
    else:
        instance.total = 0.00
pre_save.connect(pre_save_cart_receiver, sender=carts)
