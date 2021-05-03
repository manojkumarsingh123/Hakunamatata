from django.conf.urls import url
from Hakunamatata import views
# SET THE NAMESPACE!
app_name = 'Hakunamatata'
urlpatterns = [
    url(r'^contactform/$',views.contactform,name='contactform'),
    url(r'^register/$',views.register,name='register'),
    url(r'^user_login/$',views.user_login,name='user_login'),
]
