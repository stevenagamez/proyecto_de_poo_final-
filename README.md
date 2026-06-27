# Sistema Contable Profesional

## Descripción

Sistema contable desarrollado en Python aplicando los principios de Programación Orientada a Objetos (POO) y la arquitectura Modelo-Vista-Controlador (MVC). El sistema permite la autenticación de usuarios, el registro de pólizas contables, la consulta del historial de movimientos y la visualización de gráficos estadísticos mediante una interfaz gráfica.

## Objetivos

- Aplicar Programación Orientada a Objetos.
- Implementar la arquitectura MVC.
- Gestionar el registro de pólizas contables.
- Utilizar una base de datos SQLite para almacenar la información.
- Implementar autenticación segura mediante bcrypt.
- Realizar pruebas unitarias utilizando pytest.

## Tecnologías utilizadas

- Python 3.10 o superior
- SQLite
- CustomTkinter
- Matplotlib
- bcrypt
- pytest

## Librerías externas

Las siguientes librerías deben instalarse mediante `requirements.txt`:

- customtkinter
- matplotlib
- bcrypt
- pytest

## Estructura del proyecto

```
proyecto_de_poo_final/
│
├── sistema_contable/
│   ├── app/
│   │   ├── controllers/
│   │   ├── models/
│   │   ├── views/
│   │   └── main.py
│   │
│   ├── docs/
│   │   ├── diagrama_clases.png
│   │   ├── proceso_desarrollo.md
│   │   └── capturas/
│   │       ├── login.png
│   │       ├── dashboard.png
│   │       ├── registro_poliza.png
│   │       ├── grafico.png
│   │       └── pytest.png
│   │
│   ├── tests/
│   │   ├── test_poliza.py
│   │   └── test_usuario.py
│   │
│   ├── requirements.txt
│   └── README.md
```

## Requisitos

- Python 3.10 o superior
- Git
- pip

## Instalación

Clonar el repositorio:

```bash
git clone https://github.com/stevenagamez/proyecto_de_poo_final-.git
```

Ingresar al proyecto:

```bash
cd proyecto_de_poo_final-/sistema_contable
```

Instalar las dependencias:

```bash
pip install -r requirements.txt
```

## Ejecución del proyecto

Desde la carpeta `sistema_contable` ejecutar:

```bash
python -m app.main
```

También es posible ejecutar:

```bash
python app/main.py
```

## Ejecución de pruebas

Desde la carpeta `sistema_contable` ejecutar:

```bash
pytest
```

Las pruebas incluyen:

- Dos pruebas válidas para el modelo Poliza.
- Una prueba inválida para el modelo Poliza.
- Dos pruebas válidas para el modelo Usuario.
- Una prueba inválida para el modelo Usuario.

## Usuario predeterminado

Al ejecutar la aplicación por primera vez se crea automáticamente el siguiente usuario:

Usuario:

```
admin
```

Contraseña:

```
admin123
```

## Arquitectura del proyecto

El proyecto sigue el patrón Modelo-Vista-Controlador (MVC).

### Modelo

Contiene las clases que representan las entidades del sistema:

- Usuario
- Cuenta
- Poliza

Estas clases encapsulan la lógica del negocio y las validaciones.

### Vista

Implementada mediante CustomTkinter.

Contiene:

- Ventana de inicio de sesión.
- Panel principal.
- Registro de pólizas.
- Tabla del libro diario.
- Visualización gráfica de datos.

### Controlador

Administra la comunicación entre la interfaz y los modelos.

Sus principales funciones son:

- Autenticar usuarios.
- Registrar pólizas.
- Consultar información almacenada.
- Gestionar la base de datos SQLite.

## Programación Orientada a Objetos

El proyecto implementa los principales conceptos de POO:

- Clases
- Objetos
- Encapsulamiento
- Abstracción
- Separación de responsabilidades

## Diagrama de clases

El diagrama de clases se encuentra disponible en:

```
docs/diagrama_clases.png
```

Describe las relaciones entre las clases principales del sistema y la implementación de la arquitectura MVC.

## Capturas del funcionamiento

Las evidencias del funcionamiento del sistema se encuentran en:

```
docs/capturas/
```

Esta carpeta incluye:

- Inicio de sesión.
- Dashboard principal.
- Registro de pólizas.
- Tabla de movimientos.
- Gráfico estadístico.
- Ejecución de las pruebas con pytest.

## Proceso de desarrollo

La documentación completa del proceso de desarrollo se encuentra en:

```
docs/proceso_desarrollo.md
```

En este documento se describen:

- Planeación del proyecto.
- Diseño de la arquitectura.
- Desarrollo de los modelos.
- Implementación del controlador.
- Construcción de la interfaz.
- Integración con SQLite.
- Uso de bcrypt.
- Implementación de gráficos.
- Desarrollo de pruebas unitarias.
- Problemas encontrados y soluciones.
- Evidencias del desarrollo.

## Resultados

El sistema desarrollado permite:

- Iniciar sesión mediante autenticación segura.
- Registrar pólizas contables.
- Consultar el historial de movimientos.
- Visualizar información mediante gráficos.
- Validar reglas de negocio utilizando Programación Orientada a Objetos.
- Ejecutar pruebas automatizadas con pytest.

## Autores

- Steven Andrés Agamez Orozco
- Rafael Saltarín Escobar
- Handt Torres
- José Maldonado
- Disney Mercado

## Repositorio

https://github.com/stevenagamez/proyecto_de_poo_final-.git
