from django.contrib import admin
from user.models import User
from django.contrib.auth.admin import UserAdmin
from django.contrib.auth import get_user_model


User = get_user_model()


class AdminsUserAdmin(UserAdmin):
    list_display = ('email', 'first_name', 'last_name',
                    'is_active', 'is_staff', 'is_superuser','roles')
    search_fields = ('email', 'roles')
    list_filter = ('roles', 'is_active', 'is_staff', 'is_superuser')
    fieldsets = UserAdmin.fieldsets + (
        ('Role', {
            'fields': ['roles']
        }),
    )


admin.site.register(User, AdminsUserAdmin)