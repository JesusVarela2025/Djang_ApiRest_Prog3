from django.db import models
from django.core.validators import MinValueValidator
from decimal import Decimal

class Empleado(models.Model):
    idEmpleado = models.AutoField(
        primary_key=True,
        verbose_name='ID Empleado'
    )
    nombre = models.CharField(
        max_length=100,
        null=False,
        blank=False,
        verbose_name='Nombre'
    )
    departamento = models.CharField(
        max_length=100,
        null=False,
        blank=False,
        verbose_name='Departamento'
    )
    sueldo = models.DecimalField(
        max_digits=10,
        decimal_places=2,
        null=False,
        blank=False,
        validators=[MinValueValidator(Decimal('0.01'))],
        verbose_name='Sueldo'
    )
 
    class Meta:
        db_table = 'empleado'
        verbose_name = 'Empleado'
        verbose_name_plural = 'Empleados'
        ordering = ['idEmpleado']
 
    def __str__(self):
        return f'{self.nombre} - {self.departamento}'
