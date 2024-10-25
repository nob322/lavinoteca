from modelos.entidadvineria import EntidadVineria  # Importa la clase base EntidadVineria.

class Cepa(EntidadVineria):  # Define la clase Cepa que hereda de EntidadVineria.
    
    def obtenerVinos(self):  # Método para obtener los vinos asociados a esta cepa.
        from vinoteca import Vinoteca  # Importación diferida para evitar ciclos de importación.
        return [  # Retorna una lista de vinos que contienen esta cepa.
            vino for vino in Vinoteca.obtenerVinos()  # Itera sobre todos los vinos.
            if self in vino.obtenerCepas()  # Incluye solo los vinos que tienen esta cepa.
        ]

    def convertirAJSON(self):  # Método para convertir la cepa a un diccionario JSON básico.
        """Convierte la cepa a un diccionario JSON básico."""  # Documentación del método.
        return {  # Retorna un diccionario con los detalles de la cepa.
            "id": self.obtenerId(),  # Incluye el ID de la cepa.
            "nombre": self.obtenerNombre(),  # Incluye el nombre de la cepa.
            "vinos": len(self.obtenerVinos())  # Incluye el conteo de vinos asociados a esta cepa.
        }

    def convertirAJSONFull(self):  # Método para convertir la cepa a un diccionario JSON completo.
        """Convierte la cepa a un diccionario JSON completo."""  # Documentación del método.
        return {  # Retorna un diccionario con detalles completos de la cepa.
            "id": self.obtenerId(),  # Incluye el ID de la cepa.
            "nombre": self.obtenerNombre(),  # Incluye el nombre de la cepa.
            "vinos": [  # Incluye una lista de nombres de vinos asociados a esta cepa.
                f"{vino.obtenerNombre()} ({vino.obtenerBodega().obtenerNombre()})"  # Formato: nombre del vino (nombre de la bodega).
                for vino in self.obtenerVinos()  # Itera sobre los vinos asociados a esta cepa.
            ]
        }
