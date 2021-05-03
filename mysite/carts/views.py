from django.shortcuts import render,redirect
from services.models import services
#above two used for update view
from .models import carts

from orders.models import orders

from billing.models import  BillingProfile

from addresses.forms import AddressForm

# Create your views here.
def cart_home(request):
   cart_obj ,new_obj = carts.objects.new_or_get(request)
   services = cart_obj.services.all()
   total = 0
   for x in services:
       total += x.price
   cart_obj.total = total
   cart_obj.save()
   return render(request, "carts/home.html", {"cart": cart_obj})



def cart_update(request):
    services_id = request.POST.get('services_id')

    #below we create code for handel one exception
    #we know that servies is exit if might be it not exit this is the exception hence we create try except to handel this exception
    if services_id is not None:
            try:
                services_obj = services.objects.get(id=services_id)
            except services.DoesNotExist:
                print("Show message to user, services is gone?")
                return redirect("cart:home")
            cart_obj,new_obj = carts.objects.new_or_get(request)

            if services_obj in cart_obj.services.all():
                cart_obj.services.remove(services_obj)

            else:
                cart_obj.services.add(services_obj) # cart_obj.products.add(product_id)
            request.session['cart_total'] = cart_obj.services.count() #this help to show items in number form in cart icon on navbar
    return redirect("cart:home")



def checkout_home(request):
    cart_obj, cart_created = carts.objects.new_or_get(request)
    order_obj = None
    if cart_created or cart_obj.services.count() == 0:
        return redirect("cart:home")




    else:
       order_obj, new_order_obj = orders.objects.get_or_create(cart=cart_obj)
    user = request.user
    billing_profile = None
    address_form = AddressForm()
    billing_address_form = AddressForm()
    if user.is_authenticated():
        billing_profile, billing_profile_created = BillingProfile.objects.get_or_create(user=user)
    else:
        pass
    context =  {
      "object":order_obj,
      "billing_profile":billing_profile,
      "address_form ":address_form ,
      "billing_address_form":billing_address_form,


    }
    return render (request,"carts/checkout.html",context)
