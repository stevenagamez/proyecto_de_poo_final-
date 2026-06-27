# Proceso de Desarrollo

## 1. Planeación

Se definieron los requisitos del sistema contable y la arquitectura MVC. Se establecieron las entidades principales: Usuario, Cuenta y Póliza.

## 2. Diseño

Se diseñó la estructura del proyecto utilizando el patrón Modelo-Vista-Controlador (MVC), separando la lógica de negocio, la interfaz gráfica y el controlador.

## 3. Implementación

Se desarrollaron los modelos del sistema utilizando Programación Orientada a Objetos. Posteriormente se implementó el controlador y las vistas utilizando CustomTkinter.

## 4. Integración

Se integró una base de datos SQLite para almacenar usuarios y pólizas. Para proteger las contraseñas se utilizó la librería bcrypt.

## 5. Visualización

Se implementó un gráfico de barras con Matplotlib para mostrar los últimos movimientos registrados.

## 6. Pruebas

Se desarrollaron pruebas unitarias utilizando pytest para validar la creación de pólizas y el manejo de errores.

## 7. Problemas encontrados

* Organización inicial de la arquitectura MVC.
* Configuración de SQLite.
* Integración de Matplotlib con CustomTkinter.
* Validación de contraseñas mediante bcrypt.

## 8. Evidencias

Se incluyen capturas de pantalla de:

* Inicio de sesión.
* Dashboard principal.
* Registro de pólizas.
* Gráfico generado.
* Ejecución de pruebas con pytest.
