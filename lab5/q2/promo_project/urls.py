from django.contrib import admin
from django.urls import path, include  # Ensure 'include' is added here

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('eligibility.urls')),
]
