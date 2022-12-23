from django.urls import path
from . import views

urlpatterns = [
    path('meseros_list/', views.meseros_list, name='meseros_list'),
    path('meseros_details/', views.meseros_details, name="meseros_detail"),
    path('meseros_create/', views.mesero_create, name='meseros_create'),

# URLs para las vistas basadas en clases.
    path('meseros_list_vc/', views.MeserosList.as_view(), name='meseros_list_vc'),
    path('meseros_create_vc/', views.MeserosCreate.as_view(), name='meseros_create_vc'),
    path('meseros_edit_vc/<int:pk>/', views.MeseroUpdate.as_view(), name='mesero_edit_vc'),
    path('meseros_delete_vc/<int:pk>/', views.MeseroDelete.as_view(), name='mesero_delete_vc'),

# URLs serializers
    path('mesero_list_serializer/', views.ListMeseroSerializer, name='mesero_list_srr'),

    # URLs Django RESTFRAMEWORK
    path('mesero_list_drf_def/', views.mesero_api_view, name='mesero_list_rf_def'),
    path('mesero_detail_drf_def/<int:pk>', views.mesero_detail_view, name='mesero_detail_rf_def')

]




