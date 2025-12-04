from django.contrib import admin
from .models import Auth
from django.contrib.auth.hashers import make_password

class AuthAdmin(admin.ModelAdmin):
    list_display = ('id', 'username', 'email', 'created_at')
    fields = ('username', 'email', 'password', 'created_at', 'updated_at')
    readonly_fields = ('id', 'created_at', 'updated_at')
    search_fields = ('username', 'email')

    def save_model(self, request, obj, form, change):
        if obj.password and not obj.password.startswith('pbkdf2_'):
            obj.password = make_password(obj.password)
        super().save_model(request, obj, form, change)

admin.site.register(Auth, AuthAdmin)
