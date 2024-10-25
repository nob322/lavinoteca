from abc import ABC, abstractmethod  # Importa ABC y abstractmethod para definir una clase abstracta.

class EntidadVineria(ABC):  # Define la clase EntidadVineria como una clase abstracta.
    def __init__(self, id, nombre):  # Constructor de la clase que inicializa ID y nombre.
        self._id = id  # Almacena el ID de la entidad.
        self._nombre = nombre  # Almacena el nombre de la entidad.

    def establecerNombre(self, nombre):  # Método para establecer el nombre de la entidad.
        self._nombre = nombre  # Actualiza el nombre de la entidad.

    def obtenerId(self):  # Método para obtener el ID de la entidad.
        return self._id  # Retorna el ID.

    def obtenerNombre(self):  # Método para obtener el nombre de la entidad.
        return self._nombre  # Retorna el nombre.

    def __eq__(self, otro):  # Método para comparar dos objetos de tipo EntidadVineria.
        if isinstance(otro, EntidadVineria):  # Verifica si 'otro' es una instancia de EntidadVineria.
            return self._id == otro.obtenerId()  # Compara los IDs de ambas entidades.
        return False  # Retorna False si 'otro' no es una EntidadVineria.
