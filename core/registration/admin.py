from django.contrib import admin
from .models import User, Role

@admin.register(User)
class UserAdmin(admin.ModelAdmin):

    list_display = ('first_name','middle_name','last_name', 'email', 'role', 'created_at', 'is_approved')
    list_filter = ('role', 'created_at', 'is_approved')
    search_fields = ('email', 'first_name', 'last_name')
    list_editable = ('is_approved',)

@admin.register(Role)
class RoleAdmin(admin.ModelAdmin):
    list_display = ('role',)
