from django.conf.urls import url

from .views import (
        servicesListView,
        servicesDetailSlugView )


urlpatterns = [
    url(r'^$', servicesListView.as_view(), name='list'),
    url(r'^(?P<slug>[\w-]+)/$', servicesDetailSlugView.as_view(), name='detail'),
]



#?P<slug>[\w-]+)/ is gives id for each services item
