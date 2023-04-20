from django.contrib import admin
from .models import *

# Register your models here.


class UserAdmin(admin.ModelAdmin):
    list_display = ['id', 'username', 'age',
                    'tel', 'address', 'style', 'email',  'postal_code', 'password']


admin.site.register(User, UserAdmin)