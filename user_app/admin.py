from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from .models import User, PageVisit
from import_export.admin import ExportMixin


class CustomUserAdmin(UserAdmin, ExportMixin):
    """
    Custom UserAdmin class to customize the User model in the admin interface.
    """
    list_display = ('username', 'email', 'first_name', 'last_name', 'date_of_birth', 'gender')
    fieldsets = (
        (None, {'fields': ('username', 'password')}),
        ('Personal Info', {'fields': ('first_name', 'last_name', 'email', 'date_of_birth', 'gender')}),
        ('Permissions', {'fields': ('is_active', 'is_staff', 'is_superuser', 'groups', 'user_permissions')}),
        ('Important dates', {'fields': ('last_login', 'date_joined')}),
        ('Profile', {'fields': ('profile_picture', 'phone_number', 'address')}),
    )
    actions = ['export_as_excel']


class PageVisitAdmin(admin.ModelAdmin, ExportMixin):
    """
    ModelAdmin class for the PageVisit model in the admin interface.
    """
    list_display = ('user', 'page_name', 'visit_timestamp', 'visit_duration', 'is_conversion')
    list_filter = ('user', 'is_conversion')
    search_fields = ('user__username', 'page_name')
    actions = ['export_as_excel']


admin.site.register(User, CustomUserAdmin)
admin.site.register(PageVisit, PageVisitAdmin)
