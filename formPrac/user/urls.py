from django.conf.urls import url
from . import views

app_name = 'user'

urlpatterns = [

    url(r'^$', views.login, name='login'),

    url(r'^signup/$', views.signup, name='signup'),


]