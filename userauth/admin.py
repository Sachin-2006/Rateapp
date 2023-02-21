from django.contrib import admin
from userauth.models import User,TeacherProfile
from django.contrib.auth import get_user_model

admin.site.register(User)
admin.site.register(TeacherProfile)

User = get_user_model()

class LogEntryAdmin(admin.ModelAdmin):
    list_display = ['__str__', 'user', 'action_time', 'content_type', 'object_id', 'object_repr', 'change_message']
    list_filter = ['content_type']
    search_fields = ['object_repr', 'change_message']
    date_hierarchy = 'action_time'
    readonly_fields = ['content_type', 'object_id', 'object_repr', 'action_flag', 'change_message']

    def get_queryset(self, request):
        qs = super().get_queryset(request)
        return qs.select_related('content_type', 'user')

    def user(self, obj):
        return obj.user.email
    user.admin_order_field = 'user'
    user.short_description = 'User'