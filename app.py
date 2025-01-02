import tkinter as tk
from tkinter import messagebox, ttk
import sqlite3

class GestionCalificaciones:
    def __init__(self, root):
        # Conexión a la base de datos SQLite
        self.conn = sqlite3.connect("gestion_alumnos.db")
        self.cursor = self.conn.cursor()

        # Crear tabla si no existe
        self.cursor.execute("""
        CREATE TABLE IF NOT EXISTS alumnos (
            dni TEXT PRIMARY KEY,
            apellidos TEXT NOT NULL,
            nombre TEXT NOT NULL,
            nota REAL NOT NULL,
            calificacion TEXT NOT NULL
        )
        """)
        self.conn.commit()

        root.title("Sistema de Calificaciones")

        # Configurar la ventana para iniciar a pantalla completa
        screen_width = root.winfo_screenwidth()
        screen_height = root.winfo_screenheight()
        root.geometry(f"{screen_width}x{screen_height}")

        # Crear el encabezado
        encabezado = tk.Label(root, text="Sistema de Calificaciones", bg="#4CAF50", fg="white", font=("Arial", 16, "bold"), pady=10)
        encabezado.pack(fill=tk.X)

        # Crear el contenedor principal
        contenedor = tk.Frame(root)
        contenedor.pack(fill=tk.BOTH, expand=True)

        # Crear barra lateral (aside)
        self.aside = tk.Frame(contenedor, bg="#f0f8ff", width=200)
        self.aside.pack(side=tk.LEFT, fill=tk.Y)

        # Crear área principal
        self.area_principal = tk.Frame(contenedor)
        self.area_principal.pack(side=tk.RIGHT, fill=tk.BOTH, expand=True)

        # Agregar logo en la parte superior de la barra lateral
        logo = tk.PhotoImage(file="assets/logo.png")  # Asegúrate de que el logo esté en la ruta correcta
        logo_label = tk.Label(self.aside, image=logo)
        logo_label.image = logo  # Mantener una referencia a la imagen
        logo_label.pack(pady=10)

        # Agregar texto con las instrucciones de uso
        instrucciones = (
            "Instrucciones de uso:\n"
            "1. Para introducir un alumno, haga \n clic en 'Introducir alumno'.\n"
            "2. Para modificar la nota, apellido \n o nombre, haga doble clic \n en las celdas correspondientes.\n"
            "3. Para eliminar o consultar alumnos, \n seleccione la opción adecuada."
        )
        instrucciones_label = tk.Label(self.aside, text=instrucciones, bg="#f0f8ff", font=("Arial", 10), anchor="w")
        instrucciones_label.pack(padx=10, pady=10)

        # Agregar botones al aside
        botones = [
            ("Introducir alumno", self.introducir_alumno),
            ("Eliminar alumno", self.eliminar_alumno),
            ("Consultar alumno", self.consultar_alumno),
            #("Modificar nota", self.modificar_nota),
            ("Mostrar suspensos", self.mostrar_suspensos),
            ("Mostrar aprobados", self.mostrar_aprobados),
            ("Mostrar candidatos a MH", self.mostrar_mh),
        ]

        for texto, comando in botones:
            boton = tk.Button(self.aside, text=texto, command=comando, bg="#87CEFA", fg="black", font=("Arial", 10), relief=tk.GROOVE)
            boton.pack(fill=tk.X, padx=10, pady=5)


        # Crear tabla para mostrar alumnos
        self.tabla = ttk.Treeview(self.area_principal, columns=("DNI", "Apellidos", "Nombre", "Nota", "Calificación"), show="headings")
        self.tabla.heading("DNI", text="DNI")
        self.tabla.heading("Apellidos", text="Apellidos")
        self.tabla.heading("Nombre", text="Nombre")
        self.tabla.heading("Nota", text="Nota")
        self.tabla.heading("Calificación", text="Calificación")
        self.tabla.pack(fill=tk.BOTH, expand=True)

        # Personalizar encabezados y alternar colores
        estilo = ttk.Style()
        estilo.configure("Treeview.Heading", background="#4CAF50", foreground="black", font=("Arial", 10, "bold"))
        estilo.map("Treeview", background=[("selected", "#347083")])
        self.tabla.tag_configure("oddrow", background="#f2f2f2")
        self.tabla.tag_configure("evenrow", background="#ffffff")

        # Hacer las celdas de Apellidos, Nombre y Nota editables
        self.tabla.bind("<Double-1>", self.editar_celda)

        self.mostrar_alumnos()

        # Crear footer
        footer = tk.Label(root, text="Desarrollado por David", bg="#4CAF50", fg="white", font=("Arial", 10), pady=5)
        footer.pack(fill=tk.X, side=tk.BOTTOM)

    def calcular_calificacion(self, nota):
        if nota < 5:
            return "SS"
        elif 5 <= nota < 7:
            return "AP"
        elif 7 <= nota < 9:
            return "NT"
        else:
            return "SB"

    def mostrar_alumnos(self):
        # Limpiar tabla
        for row in self.tabla.get_children():
            self.tabla.delete(row)

        # Obtener datos de la base de datos
        self.cursor.execute("SELECT * FROM alumnos")
        alumnos = self.cursor.fetchall()

        for i, alumno in enumerate(alumnos):
            tag = "oddrow" if i % 2 == 0 else "evenrow"
            self.tabla.insert("", tk.END, values=alumno, tags=(tag,))

    def editar_celda(self, event):
        item = self.tabla.identify_row(event.y)
        column = self.tabla.identify_column(event.x)

        if item and column in ("#2", "#3", "#4"):  # Permitir editar Apellidos, Nombre, Nota
            col_index = int(column.strip("#")) - 1
            valores = list(self.tabla.item(item, "values"))

            def guardar_edicion():
                nuevo_valor = entry.get()

                if col_index == 3:  # Validar nota
                    try:
                        nuevo_valor = float(nuevo_valor)
                    except ValueError:
                        messagebox.showerror("Error", "La nota debe ser un número válido.")
                        return
                    valores[col_index] = nuevo_valor
                    valores[4] = self.calcular_calificacion(nuevo_valor)  # Recalcular calificación
                else:
                    valores[col_index] = nuevo_valor

                self.cursor.execute("UPDATE alumnos SET apellidos = ?, nombre = ?, nota = ?, calificacion = ? WHERE dni = ?",
                                    (valores[1], valores[2], valores[3], valores[4], valores[0]))
                self.conn.commit()
                self.mostrar_alumnos()
                top.destroy()

            x, y, width, height = self.tabla.bbox(item, column)
            top = tk.Toplevel(self.tabla)
            top.geometry(f"{width}x{height}+{self.tabla.winfo_rootx() + x}+{self.tabla.winfo_rooty() + y}")
            top.overrideredirect(True)

            entry = tk.Entry(top)
            entry.insert(0, valores[col_index])
            entry.pack(fill=tk.BOTH, expand=True)
            entry.focus_set()
            entry.bind("<Return>", lambda e: guardar_edicion())
            entry.bind("<Escape>", lambda e: top.destroy())

    def introducir_alumno(self):
        def guardar_alumno():
            dni = entry_dni.get()
            apellidos = entry_apellidos.get()
            nombre = entry_nombre.get()
            try:
                nota = float(entry_nota.get())
            except ValueError:
                messagebox.showerror("Error", "La nota debe ser un número válido.")
                return

            calificacion = self.calcular_calificacion(nota)

            try:
                self.cursor.execute("INSERT INTO alumnos (dni, apellidos, nombre, nota, calificacion) VALUES (?, ?, ?, ?, ?)",
                                    (dni, apellidos, nombre, nota, calificacion))
                self.conn.commit()
                messagebox.showinfo("Éxito", "Alumno añadido correctamente.")
                self.mostrar_alumnos()
            except sqlite3.IntegrityError:
                messagebox.showerror("Error", "Ya existe un alumno con ese DNI.")
            ventana.destroy()

        ventana = tk.Toplevel()
        ventana.title("Introducir Alumno")

        tk.Label(ventana, text="DNI:").grid(row=0, column=0)
        entry_dni = tk.Entry(ventana)
        entry_dni.grid(row=0, column=1)

        tk.Label(ventana, text="Apellidos:").grid(row=1, column=0)
        entry_apellidos = tk.Entry(ventana)
        entry_apellidos.grid(row=1, column=1)

        tk.Label(ventana, text="Nombre:").grid(row=2, column=0)
        entry_nombre = tk.Entry(ventana)
        entry_nombre.grid(row=2, column=1)

        tk.Label(ventana, text="Nota:").grid(row=3, column=0)
        entry_nota = tk.Entry(ventana)
        entry_nota.grid(row=3, column=1)

        tk.Button(ventana, text="Guardar", command=guardar_alumno).grid(row=4, columnspan=2)

    def eliminar_alumno(self):
        def eliminar():
            dni = entry_dni.get()
            self.cursor.execute("DELETE FROM alumnos WHERE dni = ?", (dni,))
            self.conn.commit()
            if self.cursor.rowcount > 0:
                messagebox.showinfo("Éxito", "Alumno eliminado correctamente.")
                self.mostrar_alumnos()
            else:
                messagebox.showerror("Error", "No existe un alumno con ese DNI.")
            ventana.destroy()

        ventana = tk.Toplevel()
        ventana.title("Eliminar Alumno")

        tk.Label(ventana, text="DNI:").grid(row=0, column=0)
        entry_dni = tk.Entry(ventana)
        entry_dni.grid(row=0, column=1)

        tk.Button(ventana, text="Eliminar", command=eliminar).grid(row=1, columnspan=2)

    def consultar_alumno(self):
        def consultar():
            dni = entry_dni.get()
            self.cursor.execute("SELECT nota, calificacion FROM alumnos WHERE dni = ?", (dni,))
            alumno = self.cursor.fetchone()
            if alumno:
                nota, calificacion = alumno
                resultado = f"Nota: {nota}\nCalificación: {calificacion}"
                messagebox.showinfo("Información del Alumno", resultado)
            else:
                messagebox.showerror("Error", "No existe un alumno con ese DNI.")
            ventana.destroy()

        ventana = tk.Toplevel()
        ventana.title("Consultar Alumno")

        tk.Label(ventana, text="DNI:").grid(row=0, column=0)
        entry_dni = tk.Entry(ventana)
        entry_dni.grid(row=0, column=1)

        tk.Button(ventana, text="Consultar", command=consultar).grid(row=1, columnspan=2)

    def modificar_nota(self):
        def modificar():
            dni = entry_dni.get()
            try:
                nueva_nota = float(entry_nota.get())
           
            except ValueError:
                messagebox.showerror("Error", "La nota debe ser un número válido.")
                return

            calificacion = self.calcular_calificacion(nueva_nota)
            self.cursor.execute("UPDATE alumnos SET nota = ?, calificacion = ? WHERE dni = ?",
                                (nueva_nota, calificacion, dni))
            self.conn.commit()
            if self.cursor.rowcount > 0:
                messagebox.showinfo("Éxito", "Nota modificada correctamente.")
                self.mostrar_alumnos()
            else:
                messagebox.showerror("Error", "No existe un alumno con ese DNI.")
            ventana.destroy()

        ventana = tk.Toplevel()
        ventana.title("Modificar Nota")

        tk.Label(ventana, text="DNI:").grid(row=0, column=0)
        entry_dni = tk.Entry(ventana)
        entry_dni.grid(row=0, column=1)

        tk.Label(ventana, text="Nueva Nota:").grid(row=1, column=0)
        entry_nota = tk.Entry(ventana)
        entry_nota.grid(row=1, column=1)

        tk.Button(ventana, text="Modificar", command=modificar).grid(row=2, columnspan=2)

    def mostrar_suspensos(self):
        self.cursor.execute("SELECT * FROM alumnos WHERE nota < 5")
        suspensos = self.cursor.fetchall()
        if suspensos:
            resultado = "\n".join([f"{dni} {apellidos}, {nombre} {nota} {calificacion}" for dni, apellidos, nombre, nota, calificacion in suspensos])
            messagebox.showinfo("Alumnos Suspensos", resultado)
        else:
            messagebox.showinfo("Información", "No hay alumnos suspensos.")

    def mostrar_aprobados(self):
        self.cursor.execute("SELECT * FROM alumnos WHERE nota >= 5")
        aprobados = self.cursor.fetchall()
        if aprobados:
            resultado = "\n".join([f"{dni} {apellidos}, {nombre} {nota} {calificacion}" for dni, apellidos, nombre, nota, calificacion in aprobados])
            messagebox.showinfo("Alumnos Aprobados", resultado)
        else:
            messagebox.showinfo("Información", "No hay alumnos aprobados.")

    def mostrar_mh(self):
        self.cursor.execute("SELECT * FROM alumnos WHERE nota = 10")
        mh = self.cursor.fetchall()
        if mh:
            resultado = "\n".join([f"{dni} {apellidos}, {nombre} {nota} {calificacion}" for dni, apellidos, nombre, nota, calificacion in mh])
            messagebox.showinfo("Candidatos a MH", resultado)
        else:
            messagebox.showinfo("Información", "No hay candidatos a MH.")

if __name__ == "__main__":
    root = tk.Tk()
    app = GestionCalificaciones(root)
    root.mainloop()
