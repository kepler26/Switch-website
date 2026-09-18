from django.contrib import admin
from .models import LogEntry


@admin.register(LogEntry)
class LogEntryAdmin(admin.ModelAdmin):
    list_display = ('date', 'time', 'username', 'hostname', 'ip_address', 'vlan_changes', 'view_log')
    search_fields = ('date', 'time', 'username', 'hostname', 'ip_address', 'vlan_changes', 'view_log')
    list_filter = ('username', 'date')

    def has_add_permission(self, request):
        return False

    def has_change_permission(self, request, obj=None):
        return False

    def has_delete_permission(self, request, obj=None):
        return False