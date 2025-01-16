from django.contrib import admin
from .models import *


class Form_admin_list(admin.ModelAdmin):
    list_display = (
        'pk',
        'name',
        'region',
        'age',
        'phone_number',
    )
    list_display_links = (
        'pk',
        'name',
        'phone_number',
    )

class User_admin_list(admin.ModelAdmin):
    list_display = (
        'user_id',
        'user_pw'
    )
    list_display_links = (
        'user_id',
    )

class Backup_admin_list(admin.ModelAdmin):
    list_display = (
        'pk',
        'name',
        'region',
        'age',
        'phone_number',
    )
    list_display_links = (
        'pk',
        'name',
        'phone_number',
    )

admin.site.register(Form, Form_admin_list)
admin.site.register(User, User_admin_list)
admin.site.register(Backup, Backup_admin_list)
