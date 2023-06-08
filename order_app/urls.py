from django.urls import path
from . import views

app_name = 'order'

urlpatterns = [
    path('create/', views.create_order, name='create_order'),
    path('<int:pk>/', views.order_detail, name='order_detail'),
    path('<int:order_id>/item/create/', views.create_order_item, name='create_order_item'),
    path('<int:order_id>/item/<int:item_id>/update/', views.update_order_item, name='update_order_item'),
    path('<int:order_id>/item/<int:item_id>/delete/', views.delete_order_item, name='delete_order_item'),
]
