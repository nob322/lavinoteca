#api + web en un mismo archivo y al mismo tiempo
from flask_restful import Api # Api Rest
from datetime import datetime # importamos lo necesario para el calendario y reloj
from vinoteca import Vinoteca  # clase definida .
from recursos import *  # archivo tiene las clases necesarias.
import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
from flask_cors import CORS
from flask import Flask, render_template, request, redirect, url_for
import MySQLdb
from flask_mysqldb import MySQL


app = Flask(__name__)  # Crea una instancia de la aplicación Flask.
api = Api(app)  # Crea una instancia de la API RESTful sobre la aplicación Flask.
CORS(app)  # Habilita CORS para todas las rutas

# Configuración de la base de datos
# Configuración de la base de datos
app.config['MYSQL_HOST'] = 'sql10.freemysqlhosting.net'
app.config['MYSQL_USER'] = 'sql10739256'
app.config['MYSQL_PASSWORD'] = 'GwjhlilkQX'  # Reemplaza con tu contraseña real
app.config['MYSQL_DB'] = 'sql10739256'





provincias = ["Buenos Aires", "Catamarca", "Chaco", "Chubut", "Córdoba",
              "Corrientes", "Entre Ríos", "Formosa", "Jujuy", "La Pampa",
              "La Rioja", "Mendoza", "Misiones", "Neuquén", "Río Negro",
              "Salta", "San Juan", "San Luis", "Santa Cruz", "Santa Fe",
              "Santiago del Estero", "Tierra del Fuego", "Tucumán"]
# Ruta principal (/) y /index apuntando a la misma página
@app.route('/')
@app.route('/index')
def index():
  
    
    ahora = datetime.now()
    fecha = ahora.strftime("%d/%m/%Y")
    hora = ahora.strftime("%H:%M:%S")

    try:
        # Conectar a la base de datos
        db = MySQLdb.connect(
            host=app.config['MYSQL_HOST'],
            user=app.config['MYSQL_USER'],
            passwd=app.config['MYSQL_PASSWORD'],
            db=app.config['MYSQL_DB']
        )

        cur = db.cursor()
        cur.execute("SELECT * FROM eventos")  # Cambia esto según tu tabla
        eventos = cur.fetchall()
        cur.close()
        db.close()  # Asegúrate de cerrar la conexión

    except Exception as e:
        print(f"Error al obtener eventos: {e}")
        eventos = []

    return render_template('index.html', fecha=fecha, hora=hora, eventos=eventos)


#ruta para inscribirse a
@app.route('/inscribir_evento', methods=['POST'])
def inscribir_evento():
    nombre_asistente = request.form.get('nombre_asistente')
    evento_id = request.form.get('evento_id')

    if not nombre_asistente or not evento_id:
        return "Nombre asistente o evento no proporcionados", 400

    try:
        # Conectar a la base de datos
        db = MySQLdb.connect(
            host=app.config['MYSQL_HOST'],
            user=app.config['MYSQL_USER'],
            passwd=app.config['MYSQL_PASSWORD'],
            db=app.config['MYSQL_DB']
        )

        cur = db.cursor()
        # Inserta el nuevo asistente
        cur.execute("INSERT INTO inscripciones (evento_id, nombre_asistente) VALUES (%s, %s)", (evento_id, nombre_asistente))

        # Actualizar el contador de registrados en la tabla eventos
        cur.execute("UPDATE eventos SET registrados = registrados + 1 WHERE id = %s", (evento_id,))

        db.commit()
        cur.close()
        db.close()

        # Obtener la lista actualizada de eventos
        db = MySQLdb.connect(
            host=app.config['MYSQL_HOST'],
            user=app.config['MYSQL_USER'],
            passwd=app.config['MYSQL_PASSWORD'],
            db=app.config['MYSQL_DB']
        )
        cur = db.cursor()
        cur.execute("SELECT * FROM eventos")
        eventos = cur.fetchall()
        cur.close()
        db.close()

        # Renderizar solo la tabla de eventos actualizada
        return render_template('tabla_eventos.html', eventos=eventos)

    except Exception as e:
        print(f"Error al inscribir asistente: {e}")
        return "Error al inscribir asistente", 500





@app.route('/eventos')
def obtener_eventos():
    try:
        db = MySQLdb.connect(
            host=app.config['MYSQL_HOST'],
            user=app.config['MYSQL_USER'],
            passwd=app.config['MYSQL_PASSWORD'],
            db=app.config['MYSQL_DB']
        )

        cur = db.cursor()
        cur.execute("SELECT * FROM eventos")
        eventos = cur.fetchall()
        cur.close()
        db.close()
    except Exception as e:
        print(f"Error al obtener eventos: {e}")
        eventos = []

    # Renderiza solo el cuerpo de la tabla
    return render_template('tabla_eventos.html', eventos=eventos)  # Crea una nueva plantilla solo para la tabla




# Ruta para probar la conexión a la base de datos
@app.route('/test_db')
def test_db():
    try:
        db = MySQLdb.connect(
            host=app.config['MYSQL_HOST'],
            user=app.config['MYSQL_USER'],
            passwd=app.config['MYSQL_PASSWORD'],
            db=app.config['MYSQL_DB']
        )

        cur = db.cursor()
        cur.execute("SELECT VERSION()")
        version = cur.fetchone()
        cur.close()
        db.close()
        return f"Conectado a MySQL, versión: {version[0]}"
    except Exception as e:
        return f"Error al conectar a la base de datos: {str(e)}"








def enviar_email(nombre, apellido, provincia, localidad, whatsapp, email, consulta):
    smtp_server = "smtp.zoho.com"
    smtp_port = 587
    username = "dalelalitotop22@zohomail.com"
    password = "fE@8_7eearsfE-e7844"

    mensaje = MIMEMultipart()
    mensaje['From'] = username
    mensaje['To'] = "david_7isra@protonmail.com"
    mensaje['Subject'] = "Nuevo mensaje del sitio web"
    webSite = "www.lavinoteca.com.ar"

    cuerpo = f"""
    Has recibido un nuevo mensaje de contacto desde el sitio web {webSite}:
    Nombre: {nombre}
    Apellido: {apellido}
    Provincia: {provincia}
    Localidad: {localidad}
    WhatsApp: {whatsapp}
    Email: {email}
    Consulta: {consulta}
    """
    mensaje.attach(MIMEText(cuerpo, 'plain'))

    try:
        with smtplib.SMTP(smtp_server, smtp_port) as server:
            server.starttls()
            server.login(username, password)
            server.send_message(mensaje)
        print("Email enviado con éxito.")
    except Exception as e:
        print(f"Error al enviar el email: {e}")

@app.route('/enviar-formulario', methods=['POST'])
def manejar_formulario():
    nombre = request.form.get('nombre')
    apellido = request.form.get('apellido')
    provincia = request.form.get('provincia')
    localidad = request.form.get('localidad')
    whatsapp = request.form.get('whatsapp')
    email = request.form.get('email')
    consulta = request.form.get('consulta')

    print(f"Nombre: {nombre}, Apellido: {apellido}, Provincia: {provincia}, "
          f"Localidad: {localidad}, WhatsApp: {whatsapp}, Email: {email}, Consulta: {consulta}")

    try:
        enviar_email(nombre, apellido, provincia, localidad, whatsapp, email, consulta)
        return f"<i class='fa-regular fa-circle-check'></i> Email enviado de manera correcta.", 200
       #return f"<i class='far fa-envelope'></i> Email enviado de manera correcta.", 200
    except Exception as e:
        return "<i class='fa-solid fa-envelope-circle-xmark'></i> Error al enviar el email.", 500

Vinoteca.inicializar()

api.add_resource(RecursoBodega, '/api/bodegas/<id>')
api.add_resource(RecursoBodegas, '/api/bodegas')
api.add_resource(RecursoCepa, '/api/cepas/<id>')
api.add_resource(RecursoCepas, '/api/cepas')
api.add_resource(RecursoVino, '/api/vinos/<id>')
api.add_resource(RecursoVinos, '/api/vinos')

if __name__ == "__main__":
    app.run(debug=True, port=5000)
