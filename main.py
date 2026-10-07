productos = [
    {"codigo": "P001", "nombre": "Laptop Lenovo", "precio": 2500, "stock": 10},
    {"codigo": "P002", "nombre": "Mouse Logitech", "precio": 80, "stock": 25},
    {"codigo": "P003", "nombre": "Teclado Logitech", "precio": 120, "stock": 15},
    {"codigo": "P004", "nombre": "Monitor LG", "precio": 850, "stock": 8},
    {"codigo": "P005", "nombre": "Disco SSD", "precio": 350, "stock": 12},
]


def mostrar_productos():
    for producto in productos:
        print(
            producto["codigo"],
            producto["nombre"],
            producto["precio"],
            producto["stock"],
        )


def buscar_producto(codigo):
    for producto in productos:
        if producto["codigo"] == codigo:
            return producto
    return None


def calcular_inventario():
    total = 0
    for producto in productos:
        total = total + producto["precio"] * producto["stock"]
    return total


def productos_poco_stock():
    for producto in productos:
        if producto["stock"] <= 10:
            print(producto["nombre"])


class Producto:
    def __init__(self, codigo, nombre, precio, stock):
        self.codigo = codigo
        self.nombre = nombre
        self.precio = precio
        self.stock = stock

    def mostrar(self):
        print(self.codigo, self.nombre, self.precio, self.stock)

    def calcular_valor(self):
        return self.precio * self.stock


producto1 = Producto("P001", "Laptop Lenovo", 2500, 10)

producto2 = Producto("P002", "Mouse Logitech", 80, 25)


producto1.mostrar()
producto2.mostrar()


productos_caros = list(filter(lambda producto: producto.precio > 500, productos))

for producto in productos_caros:
    producto.mostrar()


nombres = list(map(lambda producto: producto.nombre, productos))

print(nombres)


def registrar_producto():
    codigo = input("Ingrese código: ")
    nombre = input("Ingrese nombre: ")

    try:
        precio = float(input("Ingrese precio: "))
        stock = int(input("Ingrese stock: "))

        nuevo_producto = Producto(codigo, nombre, precio, stock)

        productos.append(nuevo_producto)
        print("Producto registrado correctamente")

    except ValueError:
        print("Error: ingrese valores numéricos válidos")


def menu():
    while True:
        print("\n")
        print("===== TECNOSTORE =====")
        print("1. Registrar producto")
        print("2. Mostrar productos")
        print("3. Buscar producto")
        print("4. Calcular inventario")
        print("5. Productos con poco stock")
        print("6. Productos con precio mayor a 500")
        print("7. Salir")

        opcion = input("Seleccione una opción: ")

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
            print("Valor del inventario:", calcular_inventario())

        elif opcion == "5":
            productos_poco_stock()

        elif opcion == "6":
            # Implementar filtro
            pass

        elif opcion == "7":
            print("Programa finalizado")
            break

        else:
            print("Opción incorrecta")


menu()
