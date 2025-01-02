# Sistema de Calificaciones

Este es un sistema desarrollado para gestionar calificaciones de alumnos utilizando Python, Tkinter y SQLite.

## 🚀 Instrucciones de uso

1. **Introducir un alumno**: Haga clic en 'Introducir alumno' para agregar un nuevo estudiante.
2. **Modificar la nota, apellido o nombre**: Haga doble clic sobre las celdas correspondientes en la tabla para editar la información.
3. **Eliminar un alumno**: Seleccione 'Eliminar alumno' e ingrese el DNI del estudiante que desea eliminar.
4. **Consultar un alumno**: Haga clic en 'Consultar alumno' para ver las notas y calificación de un estudiante.
5. **Mostrar suspensos**: Muestra a los estudiantes con nota menor a 5.
6. **Mostrar aprobados**: Muestra a los estudiantes con nota mayor o igual a 5.
7. **Mostrar candidatos a MH**: Muestra a los estudiantes con nota 10, considerados para Mención Honorífica (MH).

## 📋 Descripción del Sistema

Este sistema utiliza una base de datos SQLite para almacenar la información de los alumnos, incluyendo:

- **DNI**: Identificación única del alumno.
- **Apellidos**: Apellidos del alumno.
- **Nombre**: Nombre del alumno.
- **Nota**: Nota final del alumno.
- **Calificación**: Calificación asignada al alumno, calculada con base en su nota.

### 🎓 Calificación

La calificación se asigna según el siguiente criterio:
- **SS**: Suspenso (nota < 5)
- **AP**: Aprobado (5 ≤ nota < 7)
- **NT**: Notable (7 ≤ nota < 9)
- **SB**: Sobresaliente (nota ≥ 9)

## 👨‍💻 Desarrollado por David Flores

Este proyecto ha sido desarrollado por **David Flores** desde **Ecuador** 🇪🇨.

## 💻 Repositorio de Código

Para más detalles sobre el código fuente, visite [GitHub](https://github.com/davikho/calificaiones/).
Para descargar el programa en formato zip, dale aquí [Comprimido](https://github.com/davikho/calificaiones/archive/refs/heads/main.zip).

---

¡Gracias por usar el Sistema de Calificaciones!

## 🎨 Diseño de la UI

El diseño de la interfaz de usuario (UI) está desarrollado utilizando **Tkinter**, una librería de Python para crear interfaces gráficas. La interfaz es simple, con una barra lateral que contiene botones para interactuar con el sistema, y una área principal que muestra los datos de los estudiantes en una tabla.

La barra lateral incluye opciones para:

- Introducir, eliminar y consultar alumnos.
- Modificar la nota, apellido o nombre de los estudiantes.
- Ver los alumnos suspendidos, aprobados o con Mención Honorífica (MH).

El área principal muestra una tabla con la información de los alumnos: **DNI**, **Apellidos**, **Nombre**, **Nota** y **Calificación**. Las celdas de **Apellidos**, **Nombre** y **Nota** son editables, lo que permite realizar cambios directamente en la tabla.

### 🖼️ Vista de la Interfaz

El sistema inicia en pantalla completa y ajusta el tamaño de la ventana automáticamente. Los botones de la barra lateral tienen un diseño simple, y la tabla de alumnos permite una fácil visualización y edición de los datos.

## 📂 Base de Datos Embebida

Este sistema utiliza **SQLite** como base de datos embebida, lo que significa que no es necesario instalar un servidor de base de datos adicional. El archivo de base de datos **gestion_alumnos.db** está incluido en el proyecto y se usa de forma local, lo que hace que el sistema sea fácil de usar de inmediato, sin configuraciones adicionales.

La base de datos contiene una tabla llamada `alumnos` con los siguientes campos:

- **DNI** (clave primaria): Identificador único de cada alumno.
- **Apellidos**: Apellidos del alumno.
- **Nombre**: Nombre del alumno.
- **Nota**: Nota final del alumno.
- **Calificación**: Calificación asignada en base a la nota del alumno.

Esto permite gestionar a los estudiantes y sus calificaciones de forma eficiente, sin necesidad de una infraestructura externa.

