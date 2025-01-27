class SistemaDeAlmacenamiento:
    def __init__(self, capacidad, ubicación):
        """
        Constructor de la clase SistemaDeAlmacenamiento.
        Inicializa los atributos del objeto y simula la inicialización del sistema.

        :param capacidad: Capacidad del sistema de almacenamiento.
        :param ubicación: Ubicación del sistema de almacenamiento.
        """
        self.capacidad = capacidad
        self.ubicación = ubicación

        # Simulación de inicialización del sistema
        print(f"Inicializando el sistema de almacenamiento en {ubicación} con capacidad {capacidad} GB...")
        # En un caso real, aquí configurarías el sistema

    def __del__(self):
        """
        Destructor de la clase SistemaDeAlmacenamiento.
        Simula la limpieza y cierre del sistema.

        Nota: En Python, el destructor se llama automáticamente cuando el objeto ya no es referenciado.
        """
        # Simulación de limpieza y cierre del sistema
        print(f"Limpieza y cierre del sistema de almacenamiento en {self.ubicación}...")
        # En un caso real, aquí limpiarías y cerrarías el sistema

    def almacenar_datos(self, datos):
        """
        Método para almacenar datos en el sistema.

        Nota: En este ejemplo, no se almacenan realmente los datos, solo se simula.
        """
        print(f"Almacenando datos '{datos}' en el sistema de almacenamiento en {self.ubicación}...")
        # En un caso real, aquí almacenarías los datos


# Ejemplo de uso
if __name__ == "__main__":
    sistema = SistemaDeAlmacenamiento(1024, "Servidor Principal")
    sistema.almacenar_datos("Información Confidencial")

    # El destructor se llama automáticamente cuando salimos del bloque
    # o cuando el objeto ya no es referenciado
    del sistema  # Forzamos el llamado al destructor para demostración
