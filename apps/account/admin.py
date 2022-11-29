from django.contrib import admin
from django.contrib.auth.admin import UserAdmin as BaseUserAdmin
from django.contrib.auth.models import Group
from .models import *
from .forms import *

class UserAdmin(BaseUserAdmin):
    form = UserChangeForm
    add_form = UserCreationForm


    list_display = ('email', 'full_name', 'is_admin')
    list_filter = ('is_admin',)

    fieldsets = (
        (None, {'fields': ('email','phone_number','full_name', 'password')}),
        ('Permissions', {'fields': ('is_active','last_login','is_admin',)}),
    )
    

    add_fieldsets = (
        (None, {
            'classes': ('wide',),
            'fields': ('email', 'phone_number','full_name', 'password1', 'password2'),
        }),
    )
    search_fields = ('email','full_name')
    ordering = ('full_name',)
    filter_horizontal = ()

admin.site.register(User,UserAdmin)
admin.site.unregister(Group)

@admin.register(OtpCode)
class OtpAdmin(admin.ModelAdmin):
    list_display = ('phone','code')
