from django.conf.urls import url
from  . import  views

urlpatterns = [
url(r'^$', views.index, name = 'index'),
url(r'^about/$', views.about, name = 'about'),
url(r'^contact/$', views.contact, name = 'contact'),
url(r'^post/new/$', views.post_new, name = 'post_new'),
url(r'^post/list/$', views.post_list, name = 'post_list'),
url(r'^post/(?P<pk>\d+)/$', views.post_detail, name = 'post_detail'),
url(r'^user/(?P<user>[\w.]+)/$', views.user_detail, name = 'user_detail')
]
