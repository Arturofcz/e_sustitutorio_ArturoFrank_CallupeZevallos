from django.forms import ModelForm

from apps.platos.models import Plato

class PlatoForm(ModelForm):
    class Meta:
        model = Plato
        fields = ('nombre', 'precio', 'descripcion', 'procedencia')