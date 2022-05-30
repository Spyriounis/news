from django.contrib import admin
from django.contrib.auth.admin import UserAdmin

from .forms import CustomUserCreationForm, CustomUserChangeForm
from .models import CustomUser


class CustomeUserAdmin(UserAdmin):
    add_form = CustomUserCreationForm
    form = CustomUserChangeForm
    model = CustomUser
    list_display = [
        "email",
        "username"
    ]
    fieldsets = UserAdmin.fieldsets + (
        ("Demographics", {
            "classes": ("collapse",),
            "fields": ("age", "gender", "origin")
            }),
        ("Physical", {
            "classes": ("collapse",),
            "fields": ("height", "weight")
        })
    )
    add_fieldsets = UserAdmin.fieldsets + (
        (None, {"fields": ("age", "gender", "origin")}),
    )


admin.site.register(CustomUser, CustomeUserAdmin)
