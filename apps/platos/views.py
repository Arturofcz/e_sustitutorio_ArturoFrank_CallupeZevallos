from django.db.models import Q
from django.shortcuts import render, redirect
from django.urls import reverse_lazy

from apps.platos.forms import PlatoForm
from apps.platos.models import Plato

from django.views.generic import ListView, DeleteView, CreateView, UpdateView


# Create your views here.

def platos_list(request):

    """Obtener todos los elementos de una tabla en la bd"""
    platos = Plato.objects.all()

    query = Q(procedencia__startswith='Per') & Q(precio__gte=20)
    platos = Plato.objects.filter(query)


    return render(request, 'platillos_list.html', context={'data': platos})

def platos_details(request):
    """Obtener todos los elementos de una tabla en la BD"""
    platos = Plato.objects.all()
    return render(request, 'platos_details.html', context={'data': platos})




def plato_create(request):
    # request.method = "POST"
    if request.method == "POST":
        print("ES UN POST")
        form = PlatoForm(request.POST)
        if form.is_valid():
            # nombre = form.cleaned_data['nombre']
            # print("Nombre: {}".format(nombre))
            # edad = form.cleaned_data['edad']
            # pais = form.cleaned_data['pais']
            try:
                form.save()
                return redirect('platos_list')
            except:
                pass
    else:
        form = PlatoForm
    return render(request, 'plato-create.html', {'form': form})

class PlatosList(ListView):
    #permission_classes = [IsAuthenticated]
    model = Plato
    template_name = 'platos_vc.html'

class PlatosCreate(CreateView):
    model = Plato
    form_class = PlatoForm
    template_name = 'plato-create.html'
    success_url = reverse_lazy('platos_list_vc')

class PlatoUpdate(UpdateView):
    model = Plato
    form_class = PlatoForm
    template_name = 'plato-update-vc.html'
    success_url = reverse_lazy('platos_list_vc')


class PlatoDelete(DeleteView):
    model = Plato
    success_url = reverse_lazy('platos_list_vc')
    template_name = 'plato-confirm-delete.html'

