from flask_restful import Resource  # Importa la clase Resource para definir recursos de la API RESTful.
from flask import request  # Importa la función request para manejar las solicitudes HTTP.

import json  # Importa el módulo JSON para trabajar con datos en formato JSON.

import vinoteca  # Importa el módulo vinoteca que contiene la lógica principal.

from modelos.bodega import Bodega  # Importa la clase Bodega desde modelos.
from modelos.cepa import Cepa  # Importa la clase Cepa desde modelos.
from modelos.vino import Vino  # Importa la clase Vino desde modelos.

class RecursoBodega(Resource):  # Define un recurso para manejar las solicitudes sobre una bodega específica.

    def get(self, id):  # Método para manejar las solicitudes GET para una bodega específica por ID.
        bodega = vinoteca.Vinoteca.buscarBodega(id)  # Busca la bodega por su ID.
        if isinstance(bodega, Bodega):  # Verifica si se encontró una bodega válida.
            return json.loads(json.dumps(bodega.convertirAJSONFull())), 200  # Retorna los datos de la bodega en formato JSON y un código de estado 200 (OK).
        else:
            return {"error": "Bodega no encontrada"}, 404  # Retorna un mensaje de error y un código de estado 404 (No encontrado).

class RecursoBodegas(Resource):  # Define un recurso para manejar las solicitudes sobre todas las bodegas.

    def get(self):  # Método para manejar las solicitudes GET para todas las bodegas.
        orden = request.args.get("orden")  # Obtiene el parámetro 'orden' de la solicitud.
        if orden:  # Si se proporciona un criterio de orden...
            reverso = request.args.get("reverso")  # Obtiene el parámetro 'reverso'.
            bodegas = vinoteca.Vinoteca.obtenerBodegas(  # Obtiene las bodegas ordenadas según el criterio.
                orden=orden, reverso=reverso == "si"  # Si 'reverso' es "si", invierte el orden.
            )
        else:
            bodegas = vinoteca.Vinoteca.obtenerBodegas()  # Obtiene la lista de bodegas sin ordenar.
        return (
            json.loads(json.dumps(bodegas, default=lambda o: o.convertirAJSON())),  # Convierte las bodegas a JSON.
            200,  # Retorna un código de estado 200 (OK).
        )

class RecursoCepa(Resource):  # Define un recurso para manejar las solicitudes sobre una cepa específica.

    def get(self, id):  # Método para manejar las solicitudes GET para una cepa específica por ID.
        cepa = vinoteca.Vinoteca.buscarCepa(id)  # Busca la cepa por su ID.
        if isinstance(cepa, Cepa):  # Verifica si se encontró una cepa válida.
            return json.loads(json.dumps(cepa.convertirAJSONFull())), 200  # Retorna los datos de la cepa en formato JSON y un código de estado 200 (OK).
        else:
            return {"error": "Cepa no encontrada"}, 404  # Retorna un mensaje de error y un código de estado 404 (No encontrado).

class RecursoCepas(Resource):  # Define un recurso para manejar las solicitudes sobre todas las cepas.

    def get(self):  # Método para manejar las solicitudes GET para todas las cepas.
        orden = request.args.get("orden")  # Obtiene el parámetro 'orden' de la solicitud.
        if orden:  # Si se proporciona un criterio de orden...
            reverso = request.args.get("reverso")  # Obtiene el parámetro 'reverso'.
            cepas = vinoteca.Vinoteca.obtenerCepas(orden=orden, reverso=reverso == "si")  # Obtiene las cepas ordenadas según el criterio.
        else:
            cepas = vinoteca.Vinoteca.obtenerCepas()  # Obtiene la lista de cepas sin ordenar.
        return (
            json.loads(json.dumps(cepas, default=lambda o: o.convertirAJSONFull())),  # Convierte las cepas a JSON.
            200,  # Retorna un código de estado 200 (OK).
        )

class RecursoVino(Resource):  # Define un recurso para manejar las solicitudes sobre un vino específico.

    def get(self, id):  # Método para manejar las solicitudes GET para un vino específico por ID.
        vino = vinoteca.Vinoteca.buscarVino(id)  # Busca el vino por su ID.
        if isinstance(vino, Vino):  # Verifica si se encontró un vino válido.
            return json.loads(json.dumps(vino.convertirAJSONFull())), 200  # Retorna los datos del vino en formato JSON y un código de estado 200 (OK).
        else:
            return {"error": "Vino no encontrado"}, 404  # Retorna un mensaje de error y un código de estado 404 (No encontrado).

class RecursoVinos(Resource):  # Define un recurso para manejar las solicitudes sobre todos los vinos.

    def get(self):  # Método para manejar las solicitudes GET para todos los vinos.
        anio = request.args.get("anio")  # Obtiene el parámetro 'anio' de la solicitud.
        if anio:  # Si se proporciona un año...
            anio = int(anio)  # Convierte el año a entero.
        orden = request.args.get("orden")  # Obtiene el parámetro 'orden'.
        if orden:  # Si se proporciona un criterio de orden...
            reverso = request.args.get("reverso")  # Obtiene el parámetro 'reverso'.
            vinos = vinoteca.Vinoteca.obtenerVinos(  # Obtiene los vinos filtrados y ordenados según el criterio.
                anio, orden=orden, reverso=reverso == "si"  # Si 'reverso' es "si", invierte el orden.
            )
        else:
            vinos = vinoteca.Vinoteca.obtenerVinos(anio)  # Obtiene la lista de vinos filtrados por año si se especificó.
        return json.loads(json.dumps(vinos, default=lambda o: o.convertirAJSON())), 200  # Convierte los vinos a JSON y retorna un código de estado 200 (OK).
