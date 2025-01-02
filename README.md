
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

Para más detalles sobre el código fuente, visite [GitHub](https://github.com).

---

¡Gracias por usar el Sistema de Calificaciones!
