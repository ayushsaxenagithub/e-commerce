from django.urls import path
from . import views

app_name = 'cart_app'

urlpatterns = [
    path('cart/', views.CartListView.as_view(), name='cart_list'),
    path('cart/create/', views.CartCreateView.as_view(), name='cart_create'),
    path('cart/<int:pk>/', views.CartDetailView.as_view(), name='cart_detail'),
    path('cart/<int:pk>/update/', views.CartUpdateView.as_view(), name='cart_update'),
    path('cart/<int:pk>/delete/', views.CartDeleteView.as_view(), name='cart_delete'),
]
