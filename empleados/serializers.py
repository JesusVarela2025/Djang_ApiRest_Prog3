from rest_framework import serializers
from .models import Empleado
from decimal import Decimal
 
 
class EmpleadoSerializer(serializers.ModelSerializer):
    """
    Serializer para el modelo Empleado.
    Convierte instancias Empleado <-> JSON.
    Incluye validaciones de negocio campo a campo.
    """
 
    class Meta:
        model = Empleado
        fields = ['idEmpleado', 'nombre', 'departamento', 'sueldo']
        read_only_fields = ['idEmpleado']  # El cliente no puede enviarlo
 
    # ── Validaciones campo a campo ──────────────────────────────────────
    def validate_nombre(self, value):
        """Nombre no puede estar vacio ni ser solo espacios."""
        value = value.strip()
        if not value:
            raise serializers.ValidationError(
                'El nombre no puede estar vacio.'
            )
        if len(value) < 2:
            raise serializers.ValidationError(
                'El nombre debe tener al menos 2 caracteres.'
            )
        return value
 
    def validate_departamento(self, value):
        """Departamento requerido, no vacio."""
        value = value.strip()
        if not value:
            raise serializers.ValidationError(
                'El departamento no puede estar vacio.'
            )
        return value
 
    def validate_sueldo(self, value):
        """Sueldo debe ser mayor que 0."""
        if value <= Decimal('0.00'):
            raise serializers.ValidationError(
                'El sueldo debe ser mayor que 0.'
            )
        return value
