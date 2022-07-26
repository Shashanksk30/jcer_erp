from django.contrib import admin
from django.urls import path, include
from django.conf.urls.static import static
from . import settings
from django.contrib.auth import views as auth_views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('info.urls')),
    path('info/', include('info.urls')),
    path('api/', include('apis.urls')),
    path('accounts/login/',
         auth_views.LoginView.as_view(template_name='info/login.html'), name='login'),
    path('accounts/logout/',
         auth_views.LogoutView.as_view(template_name='info/logout.html'), name='logout'),
]+ static(settings.MEDIA_URL, document_root = settings.MEDIA_ROOT)
