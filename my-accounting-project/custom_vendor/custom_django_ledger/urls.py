"""
URL configuration for custom_django_ledger project.

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
from django.urls import path
from . import views

app_name = 'custom_django_ledger'
urlpatterns = [    
    path('<slug:entity_slug>/category/', views.ViewCategories.as_view(), name='category_view'),
    path('<slug:entity_slug>/category/<str:msg>', views.ViewCategories.as_view(), name='category_view'),

    path('<slug:entity_slug>/category/create/', views.CreateCategory.as_view(), name='category_create'),

    path('<slug:entity_slug>/category/<int:pk>/', views.UpdateSingleCategory.as_view(), name='category_update'),
    path('<slug:entity_slug>/category/<int:pk>/<str:msg>/', views.UpdateSingleCategory.as_view(), name='category_update')
    
]
