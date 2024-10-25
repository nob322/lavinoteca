from modelos.entidadvineria import EntidadVineria  # Importa la clase base EntidadVineria.

class Bodega(EntidadVineria):  # Define la clase Bodega que hereda de EntidadVineria.
    
    def obtenerVinos(self):  # Método para obtener los vinos asociados a esta bodega.
        from vinoteca import Vinoteca  # Importación diferida para evitar ciclos de importación.
        return [  # Retorna una lista de vinos que pertenecen a esta bodega.
            vino for vino in Vinoteca.obtenerVinos()  # Itera sobre todos los vinos.
            if vino.obtenerBodega().obtenerId() == self.obtenerId()  # Incluye solo los vinos que pertenecen a esta bodega.
        ]

    def obtenerCepas(self):  # Método para obtener las cepas asociadas a los vinos de la bodega.
        """Obtiene las cepas de todos los vinos de la bodega, sin duplicados."""  # Documentación del método.
        cepas = []  # Inicializa una lista vacía para almacenar cepas.
        for vino in self.obtenerVinos():  # Itera sobre los vinos de la bodega.
            for cepa in vino.obtenerCepas():  # Itera sobre las cepas de cada vino.
                if cepa not in cepas:  # Verifica si la cepa no está ya en la lista.
                    cepas.append(cepa)  # Agrega la cepa a la lista si no está duplicada.
        return cepas  # Retorna la lista de cepas únicas.

    def convertirAJSON(self):  # Método para convertir la bodega a un diccionario JSON básico.
        """Convierte la bodega a un diccionario JSON básico."""  # Documentación del método.
        return {  # Retorna un diccionario con los detalles básicos de la bodega.
            "id": self.obtenerId(),  # Incluye el ID de la bodega.
            "nombre": self.obtenerNombre(),  # Incluye el nombre de la bodega.
            "vinos": len(self.obtenerVinos())  # Incluye el conteo de vinos asociados a esta bodega.
        }

    def convertirAJSONFull(self):  # Método para convertir la bodega a un diccionario JSON completo.
        """Convierte la bodega a un diccionario JSON completo."""  # Documentación del método.
        return {  # Retorna un diccionario con detalles completos de la bodega.
            "id": self.obtenerId(),  # Incluye el ID de la bodega.
            "nombre": self.obtenerNombre(),  # Incluye el nombre de la bodega.
            "cepas": [cepa.obtenerNombre() for cepa in self.obtenerCepas()],  # Incluye los nombres de las cepas asociadas a la bodega.
            "vinos": [vino.obtenerNombre() for vino in self.obtenerVinos()]  # Incluye los nombres de los vinos de la bodega.
        }


