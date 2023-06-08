from django.urls import path
from . import views

app_name = 'review_app'

urlpatterns = [
    path('create/', views.create_review, name='create_review'),
    path('<int:review_id>/', views.review_detail, name='review_detail'),
    path('', views.review_list, name='review_list'),
    path('<int:review_id>/update/', views.update_review, name='update_review'),
    path('<int:review_id>/delete/', views.delete_review, name='delete_review'),
]
