from django.shortcuts import render
from django.views.generic import ListView,DetailView
from django.http import HttpResponseRedirect, HttpResponse

from carts.models import carts
from .models import services
# Create your views here.
class servicesListView(ListView):  #class based view it shows list of all services
    template_name = "services/list.html"
    def get_context_data(self, *args, **kwargs):
        context = super(servicesListView, self).get_context_data(*args, **kwargs)
        return context
    def get_queryset(self, *args, **kwargs):
        request = self.request
        return services.objects.all()




class servicesDetailSlugView(DetailView):
    queryset = services.objects.all()
    template_name = "services/detail.html"

    def get_context_data(self, *args, **kwargs):
        context = super(servicesDetailSlugView, self).get_context_data(*args, **kwargs)
        cart_obj, new_obj = carts.objects.new_or_get(self.request)
        context['cart'] = cart_obj


        return context








    def get_queryset(self, *args, **kwargs):
        request = self.request
        return services.objects.all()
