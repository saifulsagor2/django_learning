from django.contrib import admin
from django.urls import path, include
from . import views   # for project-level views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.home),   # project home
    path('contact/', views.contact),  # project contact
    path('first_app/', include('first_app.urls')),  # include app urls
]
