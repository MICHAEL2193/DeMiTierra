# Alcance del MVP — DeMiTierra

## 1. Descripción general

DeMiTierra será un marketplace web orientado inicialmente a residentes internacionales en Valencia que deseen localizar y comprar productos alimentarios relacionados con su país, región o cultura de origen.

La plataforma actuará como intermediaria entre clientes y pequeños comercios locales. Los comercios podrán ofrecer sus productos, gestionar sus precios y existencias, y atender los pedidos recibidos. La plataforma proporcionará un catálogo organizado y visualmente cuidado, herramientas de búsqueda, comparación de ofertas, proceso de compra y seguimiento del estado de los pedidos.

El objetivo principal del MVP no es crear desde el inicio una plataforma comercial completa, sino desarrollar una aplicación funcional que sirva como caso de estudio para diseñar, desplegar y evaluar una arquitectura cloud-native reproducible, automatizada, observable y escalable en AWS.

## 2. Roles del sistema

### 2.1. Cliente

El cliente podrá:

* Registrarse e iniciar sesión.
* Seleccionar el idioma de la interfaz.
* Seleccionar un país o región de referencia.
* Consultar los productos disponibles.
* Buscar productos y aplicar filtros básicos.
* Acceder a la ficha maestra de cada producto.
* Comparar las ofertas de diferentes comercios.
* Seleccionar el comercio al que desea comprar.
* Añadir productos al carrito.
* Modificar cantidades o eliminar productos.
* Consultar precios, comisiones y costes de envío.
* Crear un pedido mediante un pago simulado.
* Consultar el estado de sus pedidos y subpedidos.

### 2.2. Comercio

El comercio podrá:

* Crear una cuenta de comercio.
* Completar el proceso de identificación y alta.
* Consultar el estado de verificación de su cuenta.
* Iniciar sesión en su panel una vez autorizado.
* Consultar el catálogo de productos maestros existente.
* Crear una oferta para un producto ya registrado.
* Proponer la creación de un nuevo producto cuando no exista.
* Subir imágenes y proporcionar información sobre el producto.
* Indicar precio, stock, formato y disponibilidad.
* Consultar el estado de revisión de sus solicitudes.
* Corregir una solicitud cuando el administrador pida cambios.
* Recibir pedidos.
* Consultar los productos incluidos en cada pedido.
* Cambiar el estado de los pedidos.
* Indicar un tiempo estimado de preparación y entrega.

### 2.3. Administrador

El administrador podrá:

* Revisar las solicitudes de alta de comercios.
* Comprobar la información identificativa y comercial proporcionada.
* Aprobar, rechazar, suspender o solicitar cambios a un comercio.
* Revisar las solicitudes de productos y ofertas.
* Comprobar la calidad visual de las imágenes.
* Revisar nombres, marcas, descripciones, categorías, países y formatos.
* Detectar posibles productos duplicados.
* Crear una nueva ficha maestra cuando el producto no exista.
* Asociar una oferta a una ficha maestra existente.
* Aprobar, rechazar o solicitar cambios en productos y ofertas.
* Gestionar países, categorías, comercios, productos y ofertas.
* Retirar o archivar productos y ofertas que incumplan las normas de la plataforma.

## 3. Registro, verificación y alta de comercios

La creación de una cuenta de comercio no supondrá su autorización automática para vender en DeMiTierra.

Antes de publicar productos, crear ofertas o recibir pedidos, cada comercio deberá completar un proceso de identificación y verificación administrativa.

El comercio deberá proporcionar:

* Nombre comercial.
* Razón social o nombre completo del trabajador autónomo.
* Número de identificación fiscal.
* Nombre e identificación del representante legal, cuando corresponda.
* Dirección del establecimiento.
* Teléfono y correo electrónico de contacto.
* Información de inscripción en un registro mercantil o equivalente, cuando proceda.
* Número de inscripción en el RGSEAA o en el registro autonómico de establecimientos alimentarios correspondiente.
* Dirección y zona de reparto.
* Condiciones y coste del servicio de entrega.
* Declaración responsable de cumplimiento de la normativa aplicable.
* Aceptación de las condiciones de uso para comercios.

El proceso de alta tendrá los siguientes estados:

* `DRAFT`: registro iniciado, pero no enviado a revisión.
* `PENDING_VERIFICATION`: información enviada y pendiente de revisión.
* `CHANGES_REQUIRED`: el administrador ha solicitado correcciones o información adicional.
* `APPROVED`: comercio verificado y autorizado para operar.
* `REJECTED`: solicitud de alta rechazada.
* `SUSPENDED`: comercio previamente aprobado cuya actividad ha sido suspendida.

El administrador podrá revisar la información, solicitar correcciones, aprobar, rechazar o suspender al comercio.

Solo los comercios con estado `APPROVED` podrán:

* Proponer nuevos productos.
* Crear ofertas.
* Publicar precios y stock.
* Recibir y gestionar pedidos.

La plataforma mostrará al cliente la identidad comercial del vendedor y diferenciará las responsabilidades correspondientes al comercio y a DeMiTierra.

Para el MVP se utilizarán datos y documentos ficticios. No se almacenarán documentos de identidad, certificados, números fiscales o datos bancarios reales.

## 4. Catálogo basado en productos maestros y ofertas

El catálogo utilizará dos conceptos diferenciados:

1. Producto maestro.
2. Oferta del comercio.

Este modelo permitirá mostrar cada producto una sola vez, sin impedir que diferentes comercios puedan venderlo a precios y condiciones distintas.

### 4.1. Producto maestro

El producto maestro representa la información común y permanente de un producto.

Ejemplo:

**Galletas Ducales Noel 294 g**

La ficha maestra podrá contener:

* Nombre normalizado.
* Marca.
* País o región de origen.
* Categoría.
* Peso, volumen o formato.
* Descripción general.
* Imagen principal aprobada.
* Ingredientes o información adicional.
* Código de barras, cuando esté disponible.

La ficha maestra aparecerá una sola vez en el catálogo, aunque varios comercios vendan el mismo producto.

La información del producto maestro será gestionada o validada por el administrador para mantener la coherencia y calidad visual de la plataforma.

### 4.2. Oferta del comercio

Cada comercio podrá asociar su propia oferta a un producto maestro.

La oferta incluirá:

* Comercio vendedor.
* Precio base.
* Stock disponible.
* Coste de envío.
* Tiempo estimado de preparación o entrega.
* Posibilidad de recogida en el comercio, cuando corresponda.
* Estado de disponibilidad.
* Fecha de creación y última actualización.

Ejemplo:

* Comercio A: 2,40 €, envío 4,50 € y entrega estimada de 40 minutos.
* Comercio B: 2,60 €, envío 1,99 € y entrega estimada de 25 minutos.
* Comercio C: 2,75 €, recogida gratuita y entrega estimada de 35 minutos.

El usuario podrá consultar todas las ofertas aprobadas y seleccionar la que considere más conveniente.

La aplicación podrá destacar determinadas ofertas mediante etiquetas como:

* Precio del producto más bajo.
* Menor precio total con envío.
* Entrega más rápida.
* Recogida gratuita.

La plataforma no ocultará automáticamente las demás ofertas por no tener el precio más bajo.

## 5. Flujo de publicación y moderación

Los productos y las nuevas ofertas enviadas por los comercios no se publicarán automáticamente.

El flujo será el siguiente:

1. El comercio busca el producto en el catálogo existente.
2. Si el producto existe, solicita asociar una nueva oferta.
3. Si el producto no existe, propone la creación de una ficha maestra.
4. La solicitud queda pendiente de revisión.
5. El administrador revisa la información proporcionada.
6. El administrador aprueba, rechaza o solicita cambios.
7. Solo las fichas y ofertas aprobadas serán visibles para los clientes.

Los estados de revisión serán:

* `DRAFT`
* `PENDING_REVIEW`
* `CHANGES_REQUESTED`
* `APPROVED`
* `REJECTED`
* `ARCHIVED`

### 5.1. Caso A: el producto no existe

El flujo será:

1. El comercio propone el producto.
2. Introduce el nombre, marca, categoría, país, formato y descripción.
3. Sube las imágenes.
4. El administrador comprueba la calidad del anuncio.
5. El administrador verifica que el producto no exista previamente.
6. Si se aprueba, se crea una ficha maestra.
7. Se crea la primera oferta asociada al comercio.

### 5.2. Caso B: el producto ya existe

El flujo será:

1. El comercio selecciona el producto maestro existente.
2. Introduce el precio, stock y condiciones de su oferta.
3. La oferta queda pendiente de revisión.
4. El administrador revisa la solicitud.
5. Si se aprueba, la oferta queda asociada al producto maestro.

No se creará una segunda ficha visual del mismo producto.

Los cambios cotidianos de precio y stock de una oferta ya aprobada podrán realizarse sin modificar la ficha maestra. Los cambios sustanciales en la información del producto o las imágenes podrán requerir una nueva revisión administrativa.

## 6. Control de calidad visual

La publicación de productos estará sometida a un proceso de moderación para conservar una experiencia visual consistente.

El administrador revisará:

* Calidad y resolución de las imágenes.
* Iluminación y visibilidad del producto.
* Ausencia de imágenes borrosas o deformadas.
* Nombre correcto y normalizado.
* Marca y formato.
* Categoría y país de origen.
* Claridad de la descripción.
* Posible duplicidad con productos existentes.
* Cumplimiento de las normas de publicación.

El administrador podrá:

* Aprobar la solicitud.
* Rechazarla e indicar el motivo.
* Solicitar cambios al comercio.
* Asociar la propuesta a un producto maestro existente.

Solo los productos y ofertas aprobados serán visibles en el catálogo público.

## 7. Control de duplicidades

El sistema evitará que un mismo producto aparezca varias veces en el catálogo con nombres distintos.

Por ejemplo, estas propuestas podrían representar el mismo producto:

* Ducales.
* Galletas Ducales.
* Ducales colombianas.
* Galletas Noel Ducales 294 g.

El administrador deberá asociarlas a una única ficha normalizada:

**Galletas Ducales Noel 294 g**

De esta manera se consigue:

* Mantener un catálogo visualmente limpio.
* Evitar anuncios repetidos.
* Facilitar la búsqueda al cliente.
* Permitir que varios comercios compitan.
* Conservar la libertad de elección del usuario.
* Centralizar la información común del producto.

## 8. Cálculo del precio

Cada comercio establecerá el precio base de su oferta.

La plataforma añadirá una comisión porcentual configurable.

La comisión se calculará de la siguiente manera:

`comisión = precio base × porcentaje de comisión`

El precio que verá el cliente será:

`precio final del producto = precio base + comisión`

El coste del envío se mostrará de manera independiente.

El total de una oferta será:

`total de la oferta = precio final del producto + coste de envío`

En el MVP no se realizará una liquidación económica real a los comercios. El pago será simulado o se utilizará una pasarela de pago en modo de pruebas.

La comisión será una variable configurable para poder modificarla sin cambiar el código principal de la aplicación.

## 9. Gestión del carrito y los pedidos

Un carrito podrá contener productos ofrecidos por uno o varios comercios.

Ejemplo:

* Producto A vendido por Comercio 1.
* Producto B vendido por Comercio 1.
* Producto C vendido por Comercio 2.

Durante el proceso de compra, el sistema agrupará los productos por comercio.

La compra podrá generar:

* Un pedido principal para el cliente.
* Un subpedido independiente para cada comercio.

Ejemplo:

```text
Pedido principal
├── Subpedido del Comercio 1
│   ├── Producto A
│   └── Producto B
└── Subpedido del Comercio 2
    └── Producto C
```

Cada comercio gestionará únicamente el subpedido que le corresponda.

Los estados de los subpedidos serán:

* `RECEIVED`
* `PREPARING`
* `SHIPPED`
* `DELIVERED`
* `CANCELLED`

El cliente podrá consultar el estado individual de cada subpedido.

Debido a que cada establecimiento utilizará sus propios repartidores, el coste de entrega y el tiempo estimado se calcularán por comercio.

## 10. Funcionalidades incluidas

El MVP incluirá:

* Aplicación web responsive.
* Registro y autenticación de clientes.
* Registro y verificación de comercios.
* Gestión de roles y permisos.
* Selección de idioma.
* Catálogo organizado por país o región.
* Categorías, búsqueda y filtros básicos.
* Fichas maestras de productos.
* Múltiples ofertas por producto.
* Comparación de ofertas.
* Selección del comercio por parte del cliente.
* Carrito.
* Pago simulado.
* Gestión de pedidos y subpedidos.
* Seguimiento de estados.
* Panel del comercio.
* Panel del administrador.
* Moderación de productos y ofertas.
* Control de calidad visual.
* Control de duplicidades.
* Gestión básica de stock.
* Despliegue mediante contenedores.
* Infraestructura AWS mediante Terraform.
* Pipeline CI/CD.
* Logs y métricas centralizadas.
* Dashboard y alarmas.
* Autoscaling.
* Pruebas de carga reproducibles.

## 11. Funcionalidades excluidas

No se incluirán inicialmente:

* Aplicación móvil nativa.
* Pagos reales en producción.
* Facturación fiscal.
* Liquidación automática a comercios.
* Verificación automática de documentos mediante proveedores externos.
* Almacenamiento de documentos reales.
* Seguimiento GPS del repartidor.
* Chat en tiempo real.
* Inteligencia artificial.
* Recomendaciones personalizadas.
* Sistema de valoraciones y reseñas.
* Operación en otras ciudades.
* Integración con empresas externas de reparto.
* Gestión de devoluciones comerciales reales.
* Cupones y campañas promocionales avanzadas.

Estas funcionalidades podrán plantearse como trabajo futuro.

## 12. Alcance inicial de datos

Para demostrar el funcionamiento del sistema se utilizarán datos controlados:

* Tres países o regiones iniciales.
* Entre tres y cinco comercios ficticios.
* Aproximadamente treinta productos maestros.
* Varias ofertas asociadas a algunos productos.
* Usuarios y pedidos de prueba.
* Imágenes de productos de demostración.
* Datos identificativos ficticios para el proceso de verificación.
* Diferentes precios, costes de envío y tiempos de entrega.

## 13. Criterio de éxito funcional

El MVP se considerará funcional cuando permita completar el siguiente flujo:

1. Un comercio crea una cuenta.
2. El comercio completa la solicitud de alta.
3. El administrador revisa y aprueba el comercio.
4. El comercio busca un producto en el catálogo.
5. El comercio propone una nueva ficha o solicita crear una oferta.
6. El administrador revisa la solicitud.
7. El administrador aprueba la ficha o la oferta.
8. El producto aparece una sola vez en el catálogo.
9. El cliente consulta las diferentes ofertas.
10. El cliente selecciona un comercio.
11. El cliente añade el producto al carrito.
12. El cliente crea un pedido mediante pago simulado.
13. El sistema genera los subpedidos correspondientes.
14. El comercio recibe su subpedido.
15. El comercio actualiza su estado.
16. El cliente visualiza los cambios.

## 14. Criterio de éxito técnico

La solución deberá permitir:

* Desplegar la infraestructura desde cero mediante Terraform.
* Configurar la infraestructura mediante variables y outputs documentados.
* Construir la imagen Docker de la aplicación.
* Publicar automáticamente la imagen en un registro de contenedores.
* Desplegar nuevas versiones mediante GitHub Actions.
* Ejecutar la aplicación en AWS mediante contenedores.
* Centralizar logs y métricas operativas.
* Visualizar al menos un dashboard.
* Configurar al menos dos alarmas.
* Aplicar políticas de autoscaling.
* Ejecutar pruebas de carga reproducibles.
* Medir la latencia p95 y p99.
* Medir el throughput.
* Medir la tasa de errores.
* Analizar el tiempo de reacción del autoscaling.
* Analizar la estabilidad de las políticas de escalado.
* Estimar el coste de los escenarios evaluados.

## 15. Alcance geográfico inicial

El MVP estará orientado inicialmente a comercios y clientes situados en Valencia.

Esta limitación permitirá:

* Reducir la complejidad del sistema.
* Utilizar zonas de reparto controladas.
* Simular costes y tiempos de entrega realistas.
* Concentrar la prueba del modelo de negocio.
* Mantener un alcance viable para el TFM.

La expansión a otras ciudades o países se considerará una posible evolución futura del proyecto.
