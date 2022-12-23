from django.forms import ModelForm

from apps.meseros.models import Mesero

class MeseroForm(ModelForm):
    class Meta:
        model = Mesero
        fields = ('nombre', 'edad', 'pais')

