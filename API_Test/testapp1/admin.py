from django.contrib import admin
from .models import TestModel

# Register your models here.
class TestModelAdmin(admin.ModelAdmin):
    list_display = ['name', 'description', 'phone_number']

admin.site.register(TestModel, TestModelAdmin)