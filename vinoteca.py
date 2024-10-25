import json  # Importa el módulo JSON para trabajar con archivos JSON.
from modelos.bodega import Bodega  # Importa la clase Bodega desde modelos.
from modelos.cepa import Cepa  # Importa la clase Cepa desde modelos.
from modelos.vino import Vino  # Importa la clase Vino desde modelos.

class Vinoteca:  # Define la clase Vinoteca, encargada de manejar los datos de la vinoteca.
    __archivoDeDatos = "vinoteca.json"  # Ruta al archivo JSON que contiene los datos.
    __bodegas = []  # Lista privada que almacenará las bodegas.
    __cepas = []  # Lista privada que almacenará las cepas.
    __vinos = []  # Lista privada que almacenará los vinos.

    @staticmethod
    def inicializar():  # Método estático para inicializar los datos.
        """Inicializa los datos desde el archivo JSON."""  # Documentación del método.
        datos = Vinoteca.__parsearArchivoDeDatos()  # Carga los datos desde el archivo JSON.
        Vinoteca.__convertirJsonAListas(datos)  # Convierte los datos en listas de objetos.

    @staticmethod
    def __parsearArchivoDeDatos():  # Método estático privado para parsear el archivo de datos.
        """Abre el archivo JSON, lo carga en un diccionario y lo retorna."""  # Documentación del método.
        with open(Vinoteca.__archivoDeDatos, 'r', encoding='utf-8') as archivo:  # Abre el archivo en modo lectura con codificación UTF-8.
            return json.load(archivo)  # Carga los datos del JSON y los devuelve como diccionario.

    @staticmethod
    def __convertirJsonAListas(datos):  # Método estático privado para convertir los datos JSON en listas de objetos.
        """Convierte los datos del JSON en listas de objetos."""  # Documentación del método.
        Vinoteca.__bodegas = [Bodega(**b) for b in datos["bodegas"]]  # Crea instancias de Bodega a partir de los datos del JSON y las guarda en __bodegas.
        Vinoteca.__cepas = [Cepa(**c) for c in datos["cepas"]]  # Crea instancias de Cepa a partir de los datos del JSON y las guarda en __cepas.
        Vinoteca.__vinos = [Vino(**v) for v in datos["vinos"]]  # Crea instancias de Vino a partir de los datos del JSON y las guarda en __vinos.

    @staticmethod
    def obtenerBodegas(orden=None, reverso=False):  # Método estático para obtener la lista de bodegas.
        """Retorna una lista de bodegas opcionalmente ordenada."""  # Documentación del método.
        if orden:  # Si se proporciona un criterio de orden...
            return sorted(  # Ordena la lista de bodegas.
                Vinoteca.__bodegas,  # Lista a ordenar.
                key=lambda b: getattr(b, f"obtener{orden.capitalize()}")(),  # Usa la función getattr para obtener el atributo por el que se ordenará.
                reverse=reverso  # Si reverso es True, invierte el orden.
            )
        return Vinoteca.__bodegas  # Devuelve la lista sin ordenar si no se especifica orden.

    @staticmethod
    def obtenerCepas(orden=None, reverso=False):  # Método estático para obtener la lista de cepas.
        """Retorna una lista de cepas opcionalmente ordenada."""  # Documentación del método.
        if orden:  # Si se proporciona un criterio de orden...
            return sorted(  # Ordena la lista de cepas.
                Vinoteca.__cepas,  # Lista a ordenar.
                key=lambda c: getattr(c, f"obtener{orden.capitalize()}")(),  # Usa getattr para acceder al atributo de orden dinámicamente.
                reverse=reverso  # Invierte el orden si reverso es True.
            )
        return Vinoteca.__cepas  # Devuelve la lista de cepas sin ordenar.

    @staticmethod
    def obtenerVinos(anio=None, orden=None, reverso=False):  # Método estático para obtener la lista de vinos.
        """Retorna una lista de vinos, filtrada por año y/o ordenada."""  # Documentación del método.
        vinos = Vinoteca.__vinos  # Recupera la lista completa de vinos.
        if anio is not None:  # Si se especifica un año...
            vinos = [v for v in vinos if anio in v.obtenerPartidas()]  # Filtra los vinos que contienen el año dado en sus partidas.
        if orden:  # Si se proporciona un criterio de orden...
            vinos = sorted(  # Ordena los vinos usando el atributo especificado.
                vinos,
                key=lambda v: getattr(v, f"obtener{orden.capitalize()}")(),  # Usa getattr para acceder al atributo de orden.
                reverse=reverso  # Invierte el orden si reverso es True.
            )
        return vinos  # Retorna la lista filtrada/ordenada de vinos.

    @staticmethod
    def buscarBodega(id):  # Método estático para buscar una bodega por ID.
        """Busca una bodega por ID."""  # Documentación del método.
        return next((b for b in Vinoteca.__bodegas if b.obtenerId() == id), None)  # Busca la primera bodega cuyo ID coincida con el dado.

    @staticmethod
    def buscarCepa(id):  # Método estático para buscar una cepa por ID.
        """Busca una cepa por ID."""  # Documentación del método.
        return next((c for c in Vinoteca.__cepas if c.obtenerId() == id), None)  # Busca la primera cepa cuyo ID coincida con el dado.

    @staticmethod
    def buscarVino(id):  # Método estático para buscar un vino por ID.
        """Busca un vino por ID."""  # Documentación del método.
        return next((v for v in Vinoteca.__vinos if v.obtenerId() == id), None)  # Busca el primer vino cuyo ID coincida con el dado.
