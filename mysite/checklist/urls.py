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
	url(r'^(?P<list_id>[0-9]+)/check/(?P<content_id>[0-9]+)/$', views.check_off, name = 'check_off'),
	url(r'^test/$', views.test_jquery, name = 'test_jquery'),
	url(r'^add_checklist/$', views.add_checklist, name = 'add_checklist'),
	]