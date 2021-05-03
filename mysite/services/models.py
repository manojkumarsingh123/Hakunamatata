from django.db import models
from django.urls import reverse
# Create your models here.


class services(models.Model):
    title           = models.CharField(max_length=120)
    slug            = models.SlugField(blank=True, unique=True)
    description     = models.TextField()
    price           = models.DecimalField(decimal_places=2, max_digits=20, default=39.99)#means price always show 39.99
    image           = models.ImageField(upload_to='services_img',blank=True,null=True)
    Opening_time    = models.DateTimeField()
    Contact         = models.CharField(max_length=10,blank=True,null=True)
    Address_info    = models.TextField(max_length=254,null=True)


    def get_absolute_url(self):#it give details of services when we click on any services
        #return "/products/{slug}/".format(slug=self.slug)
       return reverse("services:detail", kwargs={"slug": self.slug})

    def __str__(self):
       return self.title #means that when we save info in servies field then alwsys inside servies all info show by title which we previously used during fill the all services info filed
