from modelos.entidadvineria import EntidadVineria  # Importa la clase base EntidadVineria.

class Vino(EntidadVineria):  # Define la clase Vino que hereda de EntidadVineria.
    def __init__(self, id, nombre, bodega, cepas, partidas):  # Constructor de la clase.
        super().__init__(id, nombre)  # Llama al constructor de la clase base con id y nombre.
        self._bodega = bodega  # Almacena el ID de la bodega.
        self._cepas = cepas  # Almacena una lista de IDs de cepas.
        self._partidas = partidas  # Almacena una lista de partidas del vino.

    def obtenerBodega(self):  # Método para obtener la bodega asociada al vino.
        from vinoteca import Vinoteca  # Importación diferida para evitar ciclos de importación.
        return Vinoteca.buscarBodega(self._bodega)  # Busca y retorna la bodega correspondiente al ID.

    def obtenerCepas(self):  # Método para obtener las cepas asociadas al vino.
        from vinoteca import Vinoteca  # Importación diferida para evitar ciclos de importación.
        return [Vinoteca.buscarCepa(cepa) for cepa in self._cepas]  # Retorna una lista de cepas buscadas por su ID.

    def obtenerPartidas(self):  # Método para obtener las partidas del vino.
        return self._partidas  # Retorna la lista de partidas.

    def convertirAJSON(self):  # Método para convertir el vino a un diccionario JSON básico.
        """Convierte el vino a un diccionario JSON básico."""  # Documentación del método.
        return {
            "id": self.obtenerId(),  # Incluye el ID del vino.
            "nombre": self.obtenerNombre(),  # Incluye el nombre del vino.
            "bodega": self.obtenerBodega().obtenerNombre(),  # Incluye el nombre de la bodega.
            "cepas": [cepa.obtenerNombre() for cepa in self.obtenerCepas()],  # Incluye los nombres de las cepas.
            "partidas": self.obtenerPartidas()  # Incluye las partidas del vino.
        }

    def convertirAJSONFull(self):  # Método para convertir el vino a un diccionario JSON completo.
        """Convierte el vino a un diccionario JSON completo."""  # Documentación del método.
        return self.convertirAJSON()  # Retorna el diccionario JSON básico (no se ha implementado expansión adicional).