from django.contrib import admin
from django.contrib.auth.admin import UserAdmin


from .models import CustomUser
@admin.register(CustomUser)
class CustomUserAdmin(UserAdmin):
    # show extras in admin
    fieldsets = UserAdmin.fieldsets + (
        ('Extra info', {
            'fields': (
                'is_paid',
            )
        }),
    )
    list_display = ('username', 'email', 'first_name', 'last_name', 'is_paid')


