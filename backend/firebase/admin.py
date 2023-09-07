from django.contrib import admin
from django.contrib.auth.admin import UserAdmin

from django.contrib.auth.models import Group
admin.site.unregister(Group)

from .models import *
from .forms import *

admin.site.site_header = "Site Adminstration"
admin.site.site_title = "Site Adminstration"
admin.site.index_title = "Welcome to Admin Portal"

class CustomUserAdmin(UserAdmin):
    add_form = CustomUserCreationForm
    form = CustomUserChangeForm
    model = CustomUser

    readonly_fields = ("uuid", "date_joined", "last_login")
    list_display = ("username", 'is_staff', "last_login")
    list_filter = ("is_staff",)

    fieldsets = (
        (None, {"fields": ("uuid", "username", "password", "date_joined", "last_login")}),
        ("Permissions", {"fields": ("is_staff", "is_superuser", "user_permissions")}),
    )

    add_fieldsets = (
        (None, {
            "fields": (
                "username", "password1", "password2", "is_staff","is_superuser", "user_permissions"
            )}
        ),
    )
    search_fields = ("username",)
    ordering = ("-last_login",)


admin.site.register(CustomUser, CustomUserAdmin)