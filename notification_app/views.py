from django.shortcuts import render, redirect
from django.views.generic import ListView, View
from django.contrib.auth.mixins import LoginRequiredMixin
from .models import Notification

class NotificationListView(LoginRequiredMixin, ListView):
    model = Notification
    template_name = 'notification_app/notification_list.html'
    context_object_name = 'notifications'
    paginate_by = 10

class NotificationMarkAsReadView(LoginRequiredMixin, View):
    def post(self, request, pk):
        notification = Notification.objects.get(pk=pk)
        notification.is_read = True
        notification.save()
        return redirect('notification_app:notification_list')
