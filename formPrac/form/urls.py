
from django.conf.urls import url
from . import views


urlpatterns = [

    url(r'^$', views.get_Name, name='get_Name'),


]