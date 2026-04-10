from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('captcha_app.urls')),  # Changed 'verify/' to ''
]
