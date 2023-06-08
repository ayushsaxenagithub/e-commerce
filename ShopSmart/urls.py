"""
URL configuration for ShopSmart project.

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
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('user/', include('user_app.urls')),  # Include user_app URLs
    path('product/', include('product_app.urls')),  # Include product_app URLs
    path('cart/', include('cart_app.urls')),  # Include cart_app URLs
    path('order/', include('order_app.urls')),  # Include order_app URLs
    path('payment/', include('payment_app.urls')),  # Include payment_app URLs
    path('search/', include('search_app.urls')),  # Include search_app URLs
    path('review/', include('review_app.urls')),  # Include review_app URLs
    path('wishlist/', include('wishlist_app.urls')),  # Include wishlist_app URLs
    path('notification/', include('notification_app.urls')),  # Include notification_app URLs
]
