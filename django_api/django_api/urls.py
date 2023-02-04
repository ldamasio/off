from django.contrib import admin
from django.urls import include, path
from api import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/', include('api.urls')),
    path('ht/', include('health_check.urls')),
]
