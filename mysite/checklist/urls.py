from django.conf.urls import url

from . import views
'''
List of views

1. List "index" page - displays all of the lists available.
2  List "detail" page - displays all of the contents of a given list and give pertienent details on the items.
'''
urlpatterns = [
	# ex:/checklist/
	url(r'^$', views.index, name = 'index'),
	#url(r'^$',views.IndexView.as_view(), name = 'index'),
	# ex: /checklist/5/
	url(r'^(?P<list_id>[0-9]+)/$', views.detail, name = 'detail'),
	#url(r'^(?P<pk>[0-9]+)/$', views.DetailView.as_view(), name = 'detail'),
	# ex: /checklist/5/restuls/
	#url(r'^(?P<pk>[0-9]+)/results/$', views.ResultsView.as_view(), name = 'results'),
	# ex: /checklist/5/vote/
	#url(r'^(?P<question_id>[0-9]+)/vote/$', views.vote, name = 'vote'),
				]