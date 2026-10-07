import tkinter as tk
from tkinter import messagebox, ttk


class Producto:

    def __init__(self, codigo, nombre, precio, stock):
        self.codigo = codigo
        self.nombre = nombre
        self.precio = float(precio)
        self.stock = int(stock)

    def mostrar(self):
        print(
            f"{self.codigo:<6} | {self.nombre:<20} | "
            f"S/ {self.precio:>8.2f} | {self.stock:>5}"
        )

    def calcular_valor(self):
        return self.precio * self.stock


# Productos iniciales del caso propuesto.
productos = [
    Producto("P001", "Laptop Lenovo", 2500, 10),
    Producto("P002", "Mouse Logitech", 80, 25),
    Producto("P003", "Teclado Logitech", 120, 15),
    Producto("P004", "Monitor LG", 850, 8),
    Producto("P005", "Disco SSD", 350, 12),
]


def mostrar_productos():

    if not productos:
        print("No hay productos registrados.")
        return

    print("\nCódigo | Nombre               | Precio      | Stock")
    print("-" * 58)
    for producto in productos:
        producto.mostrar()


def buscar_producto(codigo):

    codigo = codigo.strip().upper()
    for producto in productos:
        if producto.codigo.upper() == codigo:
            return producto
    return None


def buscar_producto_por_nombre(nombre):

    nombre = nombre.strip().lower()
    for producto in productos:
        if nombre in producto.nombre.lower():
            return producto
    return None


def calcular_inventario():

    total = 0
    for producto in productos:
        total += producto.calcular_valor()
    return total


def productos_poco_stock():

    encontrados = [producto for producto in productos if producto.stock <= 10]

    if not encontrados:
        print("No hay productos con poco stock.")
        return

    print("\nProductos con poco stock:")
    for producto in encontrados:
        print(f"- {producto.nombre} (stock: {producto.stock})")


def productos_precio_mayor_500():

    productos_caros = list(filter(lambda producto: producto.precio > 500, productos))

    if not productos_caros:
        print("No hay productos con precio mayor a S/ 500.")
        return

    print("\nProductos con precio mayor a S/ 500:")
    for producto in productos_caros:
        producto.mostrar()


def obtener_nombres_productos():

    nombres = list(map(lambda producto: producto.nombre, productos))
    return nombres


def mostrar_nombres_productos():

    nombres = obtener_nombres_productos()
    print("\nNombres de productos:")
    for nombre in nombres:
        print(f"- {nombre}")


def contar_productos():

    return len(productos)


def registrar_producto():

    codigo = input("Ingrese código: ").strip().upper()
    nombre = input("Ingrese nombre: ").strip()

    if not codigo or not nombre:
        print("Error: el código y el nombre son obligatorios.")
        return

    if buscar_producto(codigo):
        print("Error: ya existe un producto con ese código.")
        return

    try:
        precio = float(input("Ingrese precio: "))
        stock = int(input("Ingrese stock: "))

        if precio <= 0:
            print("Error: el precio debe ser mayor que 0.")
            return

        if stock < 0:
            print("Error: el stock no puede ser negativo.")
            return

        nuevo_producto = Producto(codigo, nombre, precio, stock)
        productos.append(nuevo_producto)
        print("Producto registrado correctamente")

    except ValueError:
        print("Error: ingrese valores numéricos válidos")


def registrar_producto_gui(
    codigo_entry, nombre_entry, precio_entry, stock_entry, resultado
):

    codigo = codigo_entry.get().strip().upper()
    nombre = nombre_entry.get().strip()

    if not codigo or not nombre:
        messagebox.showerror("Error", "El código y el nombre son obligatorios.")
        return

    if buscar_producto(codigo):
        messagebox.showerror("Error", "Ya existe un producto con ese código.")
        return

    try:
        precio = float(precio_entry.get())
        stock = int(stock_entry.get())

        if precio <= 0:
            raise ValueError("El precio debe ser mayor que 0.")
        if stock < 0:
            raise ValueError("El stock no puede ser negativo.")

        productos.append(Producto(codigo, nombre, precio, stock))
        messagebox.showinfo("Éxito", "Producto registrado correctamente")
        limpiar_campos(codigo_entry, nombre_entry, precio_entry, stock_entry)
        mostrar_en_tabla(resultado)

    except ValueError as error:
        messagebox.showerror(
            "Error", str(error) or "Ingrese valores numéricos válidos."
        )


def limpiar_campos(codigo_entry, nombre_entry, precio_entry, stock_entry):
    codigo_entry.delete(0, tk.END)
    nombre_entry.delete(0, tk.END)
    precio_entry.delete(0, tk.END)
    stock_entry.delete(0, tk.END)


def mostrar_en_tabla(tabla, lista=None):
    """Actualiza la tabla de la interfaz."""
    lista = productos if lista is None else lista

    for item in tabla.get_children():
        tabla.delete(item)

    for producto in lista:
        tabla.insert(
            "",
            tk.END,
            values=(
                producto.codigo,
                producto.nombre,
                f"S/ {producto.precio:.2f}",
                producto.stock,
                f"S/ {producto.calcular_valor():.2f}",
            ),
        )


def crear_interfaz_grafica():

    ventana = tk.Tk()
    ventana.title("TecnoStore - Gestión de Productos")
    ventana.geometry("850x600")
    ventana.resizable(False, False)

    titulo = tk.Label(
        ventana,
        text="GESTIÓN DE PRODUCTOS",
        font=("Arial", 20, "bold"),
    )
    titulo.pack(pady=15)

    formulario = tk.Frame(ventana)
    formulario.pack(pady=5)

    tk.Label(formulario, text="Código:").grid(
        row=0, column=0, padx=8, pady=6, sticky="e"
    )
    codigo_entry = tk.Entry(formulario, width=30)
    codigo_entry.grid(row=0, column=1, padx=8, pady=6)

    tk.Label(formulario, text="Nombre:").grid(
        row=1, column=0, padx=8, pady=6, sticky="e"
    )
    nombre_entry = tk.Entry(formulario, width=30)
    nombre_entry.grid(row=1, column=1, padx=8, pady=6)

    tk.Label(formulario, text="Precio:").grid(
        row=2, column=0, padx=8, pady=6, sticky="e"
    )
    precio_entry = tk.Entry(formulario, width=30)
    precio_entry.grid(row=2, column=1, padx=8, pady=6)

    tk.Label(formulario, text="Stock:").grid(
        row=3, column=0, padx=8, pady=6, sticky="e"
    )
    stock_entry = tk.Entry(formulario, width=30)
    stock_entry.grid(row=3, column=1, padx=8, pady=6)

    marco_botones = tk.Frame(ventana)
    marco_botones.pack(pady=10)

    tabla_frame = tk.Frame(ventana)
    tabla_frame.pack(pady=10)

    columnas = ("codigo", "nombre", "precio", "stock", "valor")
    tabla = ttk.Treeview(tabla_frame, columns=columnas, show="headings", height=12)
    tabla.heading("codigo", text="Código")
    tabla.heading("nombre", text="Nombre")
    tabla.heading("precio", text="Precio")
    tabla.heading("stock", text="Stock")
    tabla.heading("valor", text="Valor inventario")

    tabla.column("codigo", width=90, anchor="center")
    tabla.column("nombre", width=220)
    tabla.column("precio", width=130, anchor="e")
    tabla.column("stock", width=80, anchor="center")
    tabla.column("valor", width=150, anchor="e")
    tabla.pack()

    def accion_mostrar():
        mostrar_en_tabla(tabla)

    def accion_buscar():

        codigo = codigo_entry.get().strip()
        nombre = nombre_entry.get().strip()

        producto = None

        # Primero intenta buscar por código.
        if codigo:
            producto = buscar_producto(codigo)

        # Si no se indicó código, busca por nombre.
        if producto is None and nombre:
            producto = buscar_producto_por_nombre(nombre)

        if producto:
            mostrar_en_tabla(tabla, [producto])

            # Carga los datos encontrados en los campos.
            codigo_entry.delete(0, tk.END)
            codigo_entry.insert(0, producto.codigo)
            nombre_entry.delete(0, tk.END)
            nombre_entry.insert(0, producto.nombre)
            precio_entry.delete(0, tk.END)
            precio_entry.insert(0, str(producto.precio))
            stock_entry.delete(0, tk.END)
            stock_entry.insert(0, str(producto.stock))

            messagebox.showinfo(
                "Búsqueda",
                f"Producto encontrado:\n{producto.codigo} - {producto.nombre}",
            )
        else:
            mostrar_en_tabla(tabla, [])
            messagebox.showwarning(
                "Búsqueda",
                "No se encontró el producto.\nIngresa un código o nombre válido.",
            )

    def accion_filtrar():
        filtrados = list(filter(lambda producto: producto.precio > 500, productos))
        mostrar_en_tabla(tabla, filtrados)

    def accion_poco_stock():
        filtrados = list(filter(lambda producto: producto.stock <= 10, productos))
        mostrar_en_tabla(tabla, filtrados)

    def accion_inventario():
        messagebox.showinfo(
            "Inventario",
            f"Valor total del inventario: S/ {calcular_inventario():.2f}",
        )

    tk.Button(
        marco_botones,
        text="REGISTRAR",
        width=14,
        command=lambda: registrar_producto_gui(
            codigo_entry, nombre_entry, precio_entry, stock_entry, tabla
        ),
    ).grid(row=0, column=0, padx=5)
    tk.Button(marco_botones, text="MOSTRAR", width=14, command=accion_mostrar).grid(
        row=0, column=1, padx=5
    )
    tk.Button(marco_botones, text="BUSCAR", width=14, command=accion_buscar).grid(
        row=0, column=2, padx=5
    )
    tk.Button(
        marco_botones, text="FILTRAR > S/ 500", width=14, command=accion_filtrar
    ).grid(row=0, column=3, padx=5)
    tk.Button(
        marco_botones, text="POCO STOCK", width=14, command=accion_poco_stock
    ).grid(row=0, column=4, padx=5)
    tk.Button(
        marco_botones, text="INVENTARIO", width=14, command=accion_inventario
    ).grid(row=0, column=5, padx=5)

    mostrar_en_tabla(tabla)
    ventana.mainloop()


def menu():

    while True:
        print("\n===== TECNOSTORE =====")
        print("1. Registrar producto")
        print("2. Mostrar productos")
        print("3. Buscar producto por código")
        print("4. Calcular inventario")
        print("5. Productos con poco stock")
        print("6. Productos con precio mayor a 500")
        print("7. Mostrar nombres de productos")
        print("8. Contar productos")
        print("9. Buscar producto por nombre")
        print("10. Abrir interfaz gráfica")
        print("11. Salir")

        opcion = input("Seleccione una opción: ").strip()

        if opcion == "1":
            registrar_producto()

        elif opcion == "2":
            mostrar_productos()

        elif opcion == "3":
            codigo = input("Ingrese código: ")
            producto = buscar_producto(codigo)
            if producto:
                producto.mostrar()
            else:
                print("Producto no encontrado")

        elif opcion == "4":
            print(f"Valor del inventario: S/ {calcular_inventario():.2f}")

        elif opcion == "5":
            productos_poco_stock()

        elif opcion == "6":
            productos_precio_mayor_500()

        elif opcion == "7":
            mostrar_nombres_productos()

        elif opcion == "8":
            print(f"Cantidad de productos: {contar_productos()}")

        elif opcion == "9":
            nombre = input("Ingrese nombre o parte del nombre: ")
            producto = buscar_producto_por_nombre(nombre)
            if producto:
                producto.mostrar()
            else:
                print("Producto no encontrado")

        elif opcion == "10":
            crear_interfaz_grafica()

        elif opcion == "11":
            print("Programa finalizado")
            break

        else:
            print("Opción incorrecta")


if __name__ == "__main__":
    menu()
