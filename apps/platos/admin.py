from django.contrib import admin
from .models import Plato
# Register your models here.
@admin.register(Plato)
class PlatoAdmin(admin.ModelAdmin):
    list_display = ('nombre','precio','descripcion')
    # ields = ('nombre',)
    # list_filter = ('nombre',)