class Venta:
    def __init__(self):
        # Inicializar cantidades y precios
        self.__cantidadA = 1
        self.__cantidadB = 2
        self.__cantidadC = 3
        self.__precioA = 12
        self.__precioB = 60
        self.__precioC = 45
        self.__id_venta = None
        self.__fecha = None
        self.__cliente = None
        self.__productos = {
            "Producto A": {"cantidad": self.__cantidadA, "precio_unitario": self.__precioA, "subtotal": self.__precioA * self.__cantidadA},
            "Producto B": {"cantidad": self.__cantidadB, "precio_unitario": self.__precioB, "subtotal": self.__precioB * self.__cantidadB},
            "Producto C": {"cantidad": self.__cantidadC, "precio_unitario": self.__precioC, "subtotal": self.__precioC * self.__cantidadC},
        }
        self.__total = self.calcular_total()

    # Método para calcular el total de la venta
    def calcular_total(self):
        return sum(
            producto["subtotal"] for producto in self.__productos.values()
        )

    # Getters para acceder a los atributos privados
    def get_id_venta(self):
        return self.__id_venta

    def get_fecha(self):
        return self.__fecha

    def get_cliente(self):
        return self.__cliente

    def get_productos(self):
        return self.__productos

    def get_total(self):
        return self.__total

    # Setters para modificar los atributos privados
    def set_id_venta(self, id_venta):
        self.__id_venta = id_venta

    def set_fecha(self, fecha):
        self.__fecha = fecha

    def set_cliente(self, cliente):
        self.__cliente = cliente

    def set_productos(self, productos):
        for producto, detalles in productos.items():
            if producto in self.__productos:
                self.__productos[producto]["cantidad"] = detalles["cantidad"]
                self.__productos[producto]["precio_unitario"] = detalles["precio_unitario"]
                # Actualizar el subtotal del producto
                self.__productos[producto]["subtotal"] = detalles["cantidad"] * detalles["precio_unitario"]
        # Recalcular el total
        self.__total = self.calcular_total()

    # Método para mostrar los detalles de la venta
    def mostrar_detalle(self):
        print(f"ID Venta: {self.__id_venta}")
        print(f"Fecha: {self.__fecha}")
        print(f"Cliente: {self.__cliente}")
        print("Productos:")
        for producto, info in self.__productos.items():
            print(f"  - {producto}: Cantidad: {info['cantidad']}, Precio Unitario: ${info['precio_unitario']:.2f}, Subtotal: ${info['subtotal']:.2f}")
        print(f"Total: ${self.__total:.2f}")
