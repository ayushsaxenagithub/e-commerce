from django.urls import path
from . import views

app_name = 'payment_app'

urlpatterns = [
    path('list/', views.payment_list, name='payment_list'),
    path('detail/<int:pk>/', views.payment_detail, name='payment_detail'),
    path('create/', views.payment_create, name='payment_create'),
    path('update/<int:pk>/', views.payment_update, name='payment_update'),
    path('delete/<int:pk>/', views.payment_delete, name='payment_delete'),
]
