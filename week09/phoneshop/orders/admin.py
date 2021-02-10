from django.contrib import admin
from .models import Orders
from rest_framework.authtoken.admin import TokenAdmin
# Register your models here.

admin.site.register(Orders)

TokenAdmin.raw_id_fields = ['user']