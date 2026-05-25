from django.urls import path
from . import views
 
urlpatterns = [
    # GET (listar) y POST (crear)
    path(
        '',                                      # -> /api/empleados/
        views.EmpleadoListCreateView.as_view(),
        name='empleado-list-create'
    ),
    # GET (obtener), PUT/PATCH (actualizar), DELETE (eliminar)
    path(
        '<int:pk>/',                             # -> /api/empleados/1/
        views.EmpleadoRetrieveUpdateDestroyView.as_view(),
        name='empleado-detail'
    ),
]
