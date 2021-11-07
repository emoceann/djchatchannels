from django.urls import path, include
from django.contrib import admin

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('main.urls')),
    path('user/', include('django.contrib.auth.urls')),
    path('user/', include('memberes.urls')),
]