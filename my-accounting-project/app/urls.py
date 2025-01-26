"""
URL configuration for app project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.1/topics/http/urls/
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
from django.urls import path, include
from .settings import DEV_MODE

urlpatterns = [
    path('admin/', admin.site.urls),
]

if DEV_MODE:
    # add new urls for development branch here
    dev_urls = [
        path('dev/ledger/', include('django_ledger.urls', namespace='django-ledger')),
        path('dev/ledger/custom/', include('custom_django_ledger.urls', namespace='custom-django-ledger')),
    ]
    urlpatterns.extend(dev_urls)

