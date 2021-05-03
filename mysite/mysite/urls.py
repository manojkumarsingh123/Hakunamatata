"""mysite URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.11/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.conf.urls import url, include
    2. Add a URL to urlpatterns:  url(r'^blog/', include('blog.urls'))
"""
from django.conf.urls import url,include
from django.contrib import admin

from Hakunamatata import views


from django.conf import settings
from django.conf.urls.static import static



urlpatterns = [
#here r is regular expression
    #url(r'^$',views.index,name='index'),
    url(r'^$',views.base,name='base'),
    url(r'^home/', views.home, name='home'),
    url(r'^Hakunamatata/',include('Hakunamatata.urls')),
    url(r'^contact/',include('Hakunamatata.urls')),#to match with include create one more url.py file

    url(r'^admin/', admin.site.urls),
    url(r'^logout/$', views.user_logout, name='logout'),

    url(r'^special/$', views.special, name='special'),
    url(r'^about/$', views.about, name='about'),

    url(r'^services/', include("services.urls", namespace='services')),
    url(r'^cart/', include("carts.urls", namespace='cart')),



]



if settings.DEBUG:
    urlpatterns = urlpatterns + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
    urlpatterns = urlpatterns + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
#with the help of these ,in card.html our images is grabed from the services models

# after this setting dont forget to import

#from django.conf import settings
#from django.conf.urls.static import static


































#from Hakunamatata .views import base,contact
#urlpatterns = [
#    url(r'^$',base,name='base'),
#    url(r'^contact/$',contact,name='contact'),
#    url(r'^admin/', admin.site.urls),
#]
