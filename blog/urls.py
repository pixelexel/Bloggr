from django.conf.urls import url
from  . import  views
from django.contrib.auth import views as auth_views

urlpatterns = [
url(r'^$', views.index, name = 'index'),
url(r'^about/$', views.about, name = 'about'),
url(r'^contact/$', views.contact, name = 'contact'),
url(r'^post/new/$', views.post_new, name = 'post_new'),
url(r'^post/list/$', views.post_list, name = 'post_list'),
url(r'^post/(?P<pk>\d+)/$', views.post_detail, name = 'post_detail'),
url(r'^user/(?P<user>[\w.]+)/$', views.user_detail, name = 'user_detail'),
url(r'^post/(?P<pk>\d+)/comment/$', views.add_comment_to_post, name='add_comment_to_post'),
url(r'^comment/(?P<pk>\d+)/approve/$', views.comment_approve, name='comment_approve'),
url(r'^comment/(?P<pk>\d+)/remove/$', views.comment_remove, name='comment_remove'),
url(r'^post/(?P<pk>\d+)/edit/$', views.post_edit, name='post_edit'),
url(r'^post/(?P<pk>\d+)/delete/$', views.post_delete, name='post_delete'),
url(r'^login/$', auth_views.login, {'template_name': 'blog/login.html'}, name='login'),
url(r'^logout/$', auth_views.logout, name='logout'),
url(r'^signup/$', views.signup, name='signup')
]
