# Djang_ApiRest_Prog3: API REST para la Gestión de Empleados
Este repositorio contiene el desarrollo del backend modular para la gestión y control de registros de personal, diseñado bajo una arquitectura desacoplada. El proyecto implementa una API REST utilizando Django y Django REST Framework (DRF), con persistencia de datos relacional en el motor MySQL.

El desarrollo del sistema se articuló de forma incremental a través de las siguientes fases de ingeniería de software:

🚀 Fases del Proyecto
🛠️ Fase Inicial: Configuración del Entorno e Infraestructura
Aislamiento de Entorno: Configuración de un entorno virtual independiente mediante el módulo venv de Python para garantizar la portabilidad del software.

Gestión de Dependencias: Instalación y congelamiento del ecosistema de librerías en requirements.txt (incluyendo Django, Django REST Framework, PyMySQL y django-cors-headers).

Control de Versiones del Framework: Resolución de conflictos de compatibilidad en el mapeo del ORM mediante el rollback controlado de Django 6.0.5 hacia la versión estable Django 4.2.16 (LTS).

📋 Fase 1: Servicio de Lectura (Listar Empleados)
Implementación del endpoint de lectura general mediante el método HTTP GET.

Configuración de la conexión e integración directa con la base de datos MySQL (rh_db) utilizando el ORM de Django para la ejecución y mapeo eficiente de consultas orientadas al listado del personal.

📥 Fase 2: Servicio de Escritura (Agregar Empleado)
Desarrollo del endpoint para la creación de recursos a través del método HTTP POST.

Procesamiento de datos estructurados en formato JSON. El sistema integra validaciones estrictas a nivel de servidor mediante la capa serializer (serializers.py), asegurando la cohesión lógica y el cumplimiento de las restricciones de los modelos antes de persistir la información en la base de datos.

✏️ Fase 3: Servicio de Actualización (Modificar Datos de Empleado)
Configuración del endpoint para la edición de registros existentes utilizando los métodos HTTP PUT / PATCH.

Reutilización y adaptación de la lógica del formulario de persistencia para interceptar los datos modificados del empleado, supliendo y actualizando los campos específicos indexados en el motor relacional.

❌ Fase 4: Servicio de Supresión (Eliminar Empleados)
Implementación del endpoint de borrado físico mediante el método HTTP DELETE, referenciado directamente a través del identificador único (ID) del empleado en la URI.

Comportamiento Estructural: El borrado remueve de forma permanente la tupla en MySQL. Debido a las propiedades intrínsecas de los campos autoincrementales, el motor no reutiliza los identificadores eliminados, generando una discontinuidad secuencial intencional que garantiza la trazabilidad histórica y la integridad de los datos relacionales.

💻 Tecnologías Utilizadas
Lenguaje: Python 3.x

Framework Principal: Django 4.2.16 (LTS)

Herramientas de API: Django REST Framework (DRF)

Base de Datos: MySQL (Codificación utf8mb4_unicode_ci)

Controlador de BD: PyMySQL

Seguridad de Red: Django CORS Headers (Intercambio de Recursos de Origen Cruzado)

Pruebas y Validación: Postman / CLI
