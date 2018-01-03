from django.conf.urls import include, url
from django.contrib import admin
from mysite.views import HomeView
from mysite.views import UserRegisterView, UserRegisterDoneView
from mysite import views 
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'^accounts/', include('django.contrib.auth.urls')),
    url(r'^$', HomeView.as_view(), name='home'),
    url(r'^board/', include('board.urls', namespace='board')),
    url(r'^accounts/register/$', UserRegisterView.as_view(), name='register'),
    url(r'^accounts/register/done/$', UserRegisterDoneView.as_view(), name='register_done'),
    url(r'^ajax/validate_username/$', views.validate_username, name="validate_username"),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)