from django.contrib import admin
from django.urls import path, include
from sms_app import views

urlpatterns = [
    path('', views.home, name='home'),
    path('admin/', admin.site.urls),
    path('', include('sms_app.urls')),
    
]