from django.conf.urls import url
from  . import  views

urlpatterns = [
url(r'^$', views.index, name = 'index'),
url(r'^about/$', views.about, name = 'about'),
url(r'^contact/$', views.contact, name = 'contact'),
url(r'^post/new/$', views.post_new, name = 'post_new')
]
