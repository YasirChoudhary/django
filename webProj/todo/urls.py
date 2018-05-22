from django.conf.urls import url
from . import views

app_name = 'todo'

urlpatterns = [

    #url(r'^$', views.start, name='start'),

    #url(r'^index/', views.index, name='index'),

     url(r'^$', views.login, name='login'),
    #url(r'^login/', views.login, name='login'),

    url(r'^addtask/$', views.addtask, name='addtask'),

   # url(r'^login/', views.login, name='login'),

    url(r'^signup/', views.signup, name='signup'),

    url(r'^(?P<id>[0-9]+)/$', views.delete, name='delete'),

    url(r'(?P<id>[0-9]+)/edit/$', views.edit, name='edit'),

    #url(r'(?P<id>[0-9]+)/update/$', views.UpdateView.as_view(), name='update')


    # url(r'^/addtask/added/$', views.added, name='added')
]
