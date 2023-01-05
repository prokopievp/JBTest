from django.contrib import admin
from django.urls import path, include

urlpatterns = [
	path('', include('JBapi.urls')),
    path('admin/', admin.site.urls),
]
