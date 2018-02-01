from django.conf.urls import url
from . import views
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    url(r'^$', views.post_list, name='index'),
    url(r'^post/(?P<pk>\d+)/$', views.post_detail, name='post_detail'),
    url(r'^post/new/$', views.post_new, name='post_new'),
    url(r'^post/(?P<pk>\d+)/edit/$', views.post_edit, name='post_edit'),
    url(r'^post/(?P<pk>\d+)/remove/$', views.post_remove, name='post_remove'),
    url(r'^search/$', views.search, name='search'),
    url(r'^post/(?P<pk>\d+)/shoplist/$', views.shopListAdd, name='test_message'),
    url(r'^showlist/$', views.shopListShow, name='show_list'),
    url(r'^script/$', views.scriptShow, name='script'),
    url(r'^resume/$', views.resumeShow, name='resume'),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)