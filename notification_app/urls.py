from django.urls import path
from .views import NotificationListView, NotificationMarkAsReadView

app_name = 'notification_app'

urlpatterns = [
    path('', NotificationListView.as_view(), name='notification_list'),
    path('mark-as-read/<int:pk>/', NotificationMarkAsReadView.as_view(), name='mark_as_read'),
]
