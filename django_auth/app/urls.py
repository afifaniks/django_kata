from django.conf.urls import url
from . import views

#TEMPLATE_URLS
app_name = 'app'

urlpatterns = [
    url(r'^register/$', views.register, name='register'),
    url('user_login/', views.user_login, name="user_login")
]
