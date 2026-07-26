# Arquitectura inicial — DeMiTierra

## 1. Objetivo

Este documento define la arquitectura técnica inicial de DeMiTierra, una aplicación web utilizada como caso de estudio para diseñar, desplegar y evaluar una arquitectura cloud-native reproducible en AWS.

La arquitectura deberá permitir:

* Desarrollo local mediante contenedores.
* Despliegue automatizado.
* Separación entre frontend, backend, base de datos y almacenamiento.
* Escalado horizontal del backend.
* Centralización de logs y métricas.
* Ejecución de pruebas de carga reproducibles.
* Aprovisionamiento de infraestructura mediante Terraform.

## 2. Estilo arquitectónico

La aplicación comenzará como un monolito modular.

El backend se desplegará como una única aplicación, pero estará organizado internamente en módulos funcionales:

* Usuarios y autenticación.
* Comercios.
* Verificación de comercios.
* Productos maestros.
* Ofertas.
* Carrito.
* Pedidos y subpedidos.
* Moderación administrativa.

Este enfoque reduce la complejidad inicial sin impedir una futura separación en microservicios.

## 3. Componentes de la aplicación

### 3.1. Frontend

Tecnología prevista:

* React.
* Vite.
* JavaScript o TypeScript.

Responsabilidades:

* Interfaz del cliente.
* Panel del comercio.
* Panel del administrador.
* Catálogo y búsqueda.
* Comparación de ofertas.
* Carrito.
* Seguimiento de pedidos.
* Comunicación con el backend mediante una API HTTP.

En AWS, los archivos compilados del frontend se almacenarán en Amazon S3 y se distribuirán mediante Amazon CloudFront.

### 3.2. Backend

Tecnología prevista:

* Python.
* FastAPI.
* SQLAlchemy.
* Alembic.
* Uvicorn.
* Pydantic.

Responsabilidades:

* Autenticación y autorización.
* Reglas de negocio.
* Gestión de comercios.
* Moderación de productos.
* Gestión de ofertas.
* Carrito y pedidos.
* Acceso a la base de datos.
* Generación de logs.
* Exposición de métricas y endpoints de salud.

El backend se empaquetará como una imagen Docker y se ejecutará en Amazon ECS mediante AWS Fargate.

### 3.3. Base de datos

Se utilizará PostgreSQL.

Durante el desarrollo local, PostgreSQL se ejecutará mediante Docker Compose.

En AWS se utilizará Amazon RDS para PostgreSQL.

La base de datos almacenará:

* Usuarios.
* Comercios.
* Estados de verificación.
* Productos maestros.
* Ofertas.
* Categorías y países.
* Pedidos y subpedidos.
* Historiales de estado.
* Registros de moderación.

### 3.4. Almacenamiento de imágenes

Las imágenes de productos se almacenarán en Amazon S3.

La base de datos no guardará directamente los archivos de imagen. Guardará únicamente referencias o claves que permitan localizarlos en S3.

Durante las primeras etapas del desarrollo local podrá utilizarse almacenamiento local o un servicio compatible con S3.

### 3.5. Balanceador de carga

El tráfico dirigido al backend pasará por un Application Load Balancer.

Sus responsabilidades serán:

* Recibir peticiones HTTP o HTTPS.
* Distribuir las peticiones entre las tareas de ECS.
* Ejecutar comprobaciones de salud.
* Proporcionar métricas de tráfico, latencia y errores.
* Permitir el escalado horizontal del backend.

### 3.6. Registro de contenedores

Amazon ECR almacenará las imágenes Docker del backend.

El flujo será:

1. GitHub Actions obtiene el código.
2. Ejecuta las pruebas.
3. Construye la imagen Docker.
4. Publica la imagen en Amazon ECR.
5. Actualiza el servicio de ECS.

### 3.7. Observabilidad

Amazon CloudWatch se utilizará para:

* Centralizar los logs del backend.
* Consultar métricas de ECS.
* Consultar métricas del balanceador.
* Crear dashboards.
* Configurar alarmas.
* Analizar errores y comportamiento bajo carga.

Inicialmente se configurarán al menos:

* Una alarma de errores HTTP 5xx o latencia elevada.
* Una alarma de saturación de CPU o memoria.
* Un dashboard operativo.

### 3.8. Autoscaling

El servicio de ECS podrá aumentar o reducir el número de tareas del backend.

Las primeras políticas evaluadas podrán utilizar:

* Utilización media de CPU.
* Utilización media de memoria.
* Número de peticiones recibidas por tarea.

Se analizarán:

* Tiempo de reacción.
* Número de tareas activas.
* Estabilidad.
* Latencia durante el escalado.
* Coste estimado.

### 3.9. Infraestructura como Código

Terraform se utilizará para crear y configurar:

* Red y subredes.
* Grupos de seguridad.
* Application Load Balancer.
* Cluster y servicio ECS.
* Definiciones de tareas.
* Repositorio ECR.
* Base de datos RDS.
* Buckets S3.
* Distribución CloudFront.
* Roles y políticas IAM.
* Logs, métricas, dashboards y alarmas.
* Políticas de autoscaling.

## 4. Arquitectura local

Durante el desarrollo se utilizará Docker Compose.

La primera arquitectura local será:

```text
Navegador
    │
    ▼
Frontend React
    │
    ▼
Backend FastAPI
    │
    ▼
PostgreSQL
```

Los componentes previstos serán:

* `frontend`
* `backend`
* `database`

El desarrollo local deberá reproducir, en la medida de lo posible, el comportamiento del entorno cloud.

## 5. Arquitectura AWS

La arquitectura inicial en AWS será:

```text
Usuario
   │
   ▼
CloudFront
   ├── Frontend almacenado en S3
   │
   └── Peticiones API
            │
            ▼
   Application Load Balancer
            │
            ▼
      ECS Fargate
      Backend FastAPI
            │
      ┌─────┴─────┐
      ▼           ▼
RDS PostgreSQL   S3 de imágenes
```

Los logs y métricas serán enviados a CloudWatch.

Las imágenes Docker se almacenarán en ECR.

Terraform gestionará la infraestructura y GitHub Actions automatizará la integración y el despliegue.

## 6. Decisiones iniciales

Se adoptan las siguientes decisiones:

* Aplicación web responsive, no aplicación móvil nativa.
* Frontend React con Vite.
* Backend FastAPI.
* Base de datos PostgreSQL.
* Monolito modular.
* API HTTP basada en REST.
* Contenedorización con Docker.
* Desarrollo local con Docker Compose.
* Despliegue del backend en ECS Fargate.
* Frontend estático en S3 y CloudFront.
* Imágenes de productos en S3.
* Infraestructura mediante Terraform.
* CI/CD mediante GitHub Actions.
* Observabilidad mediante CloudWatch.
* Pruebas de carga mediante k6.

## 7. Evolución futura

La arquitectura podrá evolucionar posteriormente mediante:

* Separación de módulos en microservicios.
* Uso de colas para procesamiento asíncrono.
* Caché distribuida.
* Notificaciones en tiempo real.
* Procesamiento automático de imágenes.
* Alta disponibilidad de la base de datos.
* Despliegues blue/green.
* Entornos independientes de desarrollo, validación y producción.
