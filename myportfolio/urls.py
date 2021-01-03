from django.contrib import admin
from django.urls import include, path

urlpatterns = [
    path('projects/', include('projects.urls')),
    path('myprofile/', include('myprofile.urls')),
    path('admin/', admin.site.urls),
]