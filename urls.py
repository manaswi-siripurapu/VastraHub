from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/', include('delivery_management.urls')), # Include your app's URLs
    # Add other app URLs here
]