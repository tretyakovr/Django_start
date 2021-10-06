"""geekshop URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.2/topics/http/urls/
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
from django.urls import path, re_path, include
from django.conf import settings
from django.conf.urls.static import static
import mainapp.views as mainapp

app_name = 'mainapp'

urlpatterns = [
    path('products_all/', mainapp.products_all, name='products_all'),
    re_path(r'^category/(?P<pk>\d+)/$', mainapp.products, name='category'),
    path('products/', include('mainapp.urls', namespace='products')),
    re_path(r'^contacts/', mainapp.contacts, name='contacts'),
    re_path(r'^$', mainapp.main, name='main'),
    re_path(r'^auth/', include('authapp.urls', namespace='auth')),
    re_path(r'^basket/', include('basketapp.urls', namespace='basket')),
    path('', include('social_django.urls', namespace='social_vk')),
    re_path(r'^auth/verify/google/oauth2/', include("social_django.urls", namespace="social_google")),
    re_path(r'^admin/', include('adminapp.urls', namespace='admin')),
    re_path(r'^order/', include('ordersapp.urls', namespace='order')),
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root = settings.MEDIA_ROOT)
