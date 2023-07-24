"""
URL configuration for hospitalmanagement project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path,include
from doctor.views import *
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('admin/', admin.site.urls),
    path('',HomeView.as_view(),name="home"),
    path('about',AboutView.as_view(),name="about"),
    path('blog',BlogView.as_view(),name="blog"),
    path('contact',ContactView.as_view(),name="contact"),
    path('gallery',GalleryView.as_view(),name="gallery"),
    path('service',ServiceView.as_view(),name="service"),
    path('navbar',NavbarView.as_view(),name="nav"),
    path('doc/',include('doctor.urls')),
    path('pat/',include('patient.urls')),
    path('logout',LgOut.as_view(),name="logout"),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
