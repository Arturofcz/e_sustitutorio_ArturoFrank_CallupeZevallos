from django.contrib import admin
from .models import Comensales
# Register your models here.

@admin.register(Comensales)
class ComensalesAdmin(admin.ModelAdmin):
    list_display = ('nombre','edad','direccion')

