from django.conf import settings
from django.conf.urls.static import static

"""Overseasdreamhome URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.1/topics/http/urls/
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
from django.urls import path
from ecommerceApp.views import home, CheapHomes, DreamHomes, ContactUs, properties, about
urlpatterns = [
    path('admin/', admin.site.urls),
    path('', home),
    path('CheapHomes', CheapHomes),
    path('DreamHomes', DreamHomes),
    path('ContactUs', ContactUs),
    path('AboutUs', about),
    path('property/CheapHomes', CheapHomes),
    path('property/DreamHomes', DreamHomes),
    path('property/ContactUs', ContactUs),
    path('property/AboutUs', about),
    path('property/property/CheapHomes', CheapHomes),
    path('property/property/DreamHomes', DreamHomes),
    path('property/property/ContactUs', ContactUs),
    path('property/property/AboutUs', about),
    path('property/<str:id>', properties),
    path('property/property/<str:id>', properties),
    path('property/property/property/<str:id>', properties),
    
]+ static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
