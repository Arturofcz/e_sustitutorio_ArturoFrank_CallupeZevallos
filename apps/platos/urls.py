from django.urls import path
from . import views

urlpatterns = [
    path('platos_list/', views.platos_list, name='platos_list'),
    path('platos_details/', views.platos_details, name="platos_detail"),
    path('platos_create/', views.plato_create, name='platos_create'),

# URLs para las vistas basadas en clases.
    path('platos_list_vc/', views.PlatosList.as_view(), name='platos_list_vc'),
    path('platos_create_vc/', views.PlatosCreate.as_view(), name='plato_create_vc'),
    path('platos_edit_vc/<int:pk>/', views.PlatoUpdate.as_view(), name='plato_edit_vc'),
    path('platos_delete_vc/<int:pk>/', views.PlatoDelete.as_view(), name='plato_delete_vc'),
]