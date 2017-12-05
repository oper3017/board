from django.conf.urls import include, url
from django.contrib import admin
from mysite.views import HomeView


urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'^accounts/', include('django.contrib.auth.urls')),
    url(r'^$', HomeView.as_view(), name='home'),
    url(r'^board/', include('board.urls', namespace='board')),
    
]