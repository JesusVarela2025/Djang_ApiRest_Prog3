from django.shortcuts import render
from rest_framework import generics, status
from rest_framework.response import Response
from .models import Empleado
from .serializers import EmpleadoSerializer
 
 
class EmpleadoListCreateView(generics.ListCreateAPIView):
    """
    GET  /api/empleados/     -> Lista todos los empleados
    POST /api/empleados/     -> Crea un nuevo empleado
    """
    queryset = Empleado.objects.all()
    serializer_class = EmpleadoSerializer
 
    def list(self, request, *args, **kwargs):
        """Retorna lista de empleados con metadata."""
        queryset = self.get_queryset()
        serializer = self.get_serializer(queryset, many=True)
        return Response({
            'success': True,
            'total': queryset.count(),
            'empleados': serializer.data
        }, status=status.HTTP_200_OK)
 
    def create(self, request, *args, **kwargs):
        """Crea empleado y retorna 201 Created."""
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response({
            'success': True,
            'mensaje': 'Empleado creado exitosamente.',
            'empleado': serializer.data
        }, status=status.HTTP_201_CREATED)
 
 
class EmpleadoRetrieveUpdateDestroyView(generics.RetrieveUpdateDestroyAPIView):
    """
    GET    /api/empleados/{id}/  -> Obtiene un empleado
    PUT    /api/empleados/{id}/  -> Actualiza completamente
    PATCH  /api/empleados/{id}/  -> Actualiza parcialmente
    DELETE /api/empleados/{id}/  -> Elimina
    """
    queryset = Empleado.objects.all()
    serializer_class = EmpleadoSerializer
    lookup_field = 'pk'
 
    def retrieve(self, request, *args, **kwargs):
        instance = self.get_object()
        serializer = self.get_serializer(instance)
        return Response({'success': True, 'empleado': serializer.data})
 
    def update(self, request, *args, **kwargs):
        partial = kwargs.pop('partial', False)
        instance = self.get_object()
        serializer = self.get_serializer(
            instance, data=request.data, partial=partial)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response({
            'success': True,
            'mensaje': 'Empleado actualizado exitosamente.',
            'empleado': serializer.data
        })
 
    def destroy(self, request, *args, **kwargs):
        instance = self.get_object()
        instance.delete()
        return Response({
            'success': True,
            'mensaje': 'Empleado eliminado exitosamente.'
        }, status=status.HTTP_200_OK)
