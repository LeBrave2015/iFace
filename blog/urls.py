from django.conf.urls import url
from . import views

urlpatterns = [
	url(r'^$', views.post_list, name='post_list'),
	url(r'^post/(?P<pk>[0-9]+)/$', views.post_detail, name='post_detail'),
	url(r'^name/(?P<pk>[0-9]+)/$', views.post_detail_detail, name='post_detail_detail'), 
	url(r'^add/$', views.add, name='add'),
        url(r'^image/$', views.image, name='imagine'),
]
