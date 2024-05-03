from django.contrib import admin
from django.urls import path, include

urlpatterns = [
	path('private/2803', admin.site.urls),
	path('', include('web.urls')),
]
