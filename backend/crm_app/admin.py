from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from .models import *
from django.contrib.auth.forms import UserChangeForm
from django import forms


class CustomUserChangeForm(UserChangeForm):
    class Meta(UserChangeForm.Meta):
        model = CustomUser

    # Override the password field to make it read-only
    password = forms.CharField(label="Password", widget=forms.TextInput(attrs={'readonly': 'readonly'}))

class CustomUserAdmin(UserAdmin):
    form = CustomUserChangeForm  # Use the custom form here
    list_display = ('username', 'email', 'first_name', 'last_name', 'is_staff')

admin.site.register(CustomUser, CustomUserAdmin)
admin.site.register(Customer)
admin.site.register(Order)
admin.site.register(Product)