from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'$', views.post_list, name='post_list'),
    url(r'^post/(?P<pk>\d+)/$', views.post_detail, name='post_detail'),
    url(r'^articles', views.article_list, name='article_list'),
    url(r'^article/(?P<pk>\d+)/$', views.article_detail, name='article_detail'),
]