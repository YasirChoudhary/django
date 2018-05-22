from django.conf.urls import url

'''
->django 			package
	->conf			package
		->urls 		module name
			->url 	method name

url method can take 4 arguments

url(regex, view, kwargs=None, name=None)
'''

from . import views


app_name = 'polls'

urlpatterns =[

	url(r'^$', views.IndexView.as_view(), name='index'),
	url(r'^(?P<pk>[0-9]+)/$', views.DetailView.as_view(), name='detail'),
	url(r'^(?P<pk>[0-9]+)/results/$', views.ResultView.as_view(), name='results'),
	url(r'^(?P<question_id>[0-9]+)/vote/$', views.vote, name='vote'),
]

'''
urlpatterns = [
	url(r'^$', views.index, name='index'),
#	url(r'test/$', views.test, name='test'),

	# ex: /polls/5/
	url(r'^(?P<question_id>[0-9]+)/$', views.detail, name='detail'),

	# ex: /polls/5/results/
	url(r'^(?P<question_id>[0-9]+)/results/$', views.results, name='result'),

	 # ex: /polls/5/vote/
	url(r'^(?P<question_id>[0-9]+)/vote/$', views.vote, name='vote'),


]
'''
