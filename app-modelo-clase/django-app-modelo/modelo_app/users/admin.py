from django.contrib import admin
from .models import User, UserAddress

@admin.register(User)
class UserAdmin(admin.ModelAdmin):
    list_display = ("name", "email", "age", "rfc", "created_date")
    search_fields = ("name", "email", "rfc")
    list_filter = ("created_date", "updated_date")
    ordering = ("-created_date",)

@admin.register(UserAddress)
class UserAddressAdmin(admin.ModelAdmin):
    list_display = ("user", "street", "city", "country", "zip_code", "created_date")
    search_fields = ("street", "city", "country", "zip_code")
    list_filter = ("country", "created_date")
    ordering = ("-created_date",)
