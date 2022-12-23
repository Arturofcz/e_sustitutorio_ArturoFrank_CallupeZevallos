from django.contrib import admin
from .models import Mesero
# Register your models here.
@admin.register(Mesero)
class MeseroAdmin(admin.ModelAdmin):
    list_display = ('nombre','edad','direccion')