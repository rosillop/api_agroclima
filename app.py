import os
from flask import Flask, request, jsonify
from dotenv import load_dotenv
from modelo_sensor import LecturaSensor

load_dotenv()
servidor_web = Flask(__name__)
historial_lecturas = []

nombre_empresa = os.environ.get("NOMBRE_EMPRESA", "AgroClima Lambayeque")
modo_sistema = os.environ.get("MODO_SISTEMA", "PRODUCCION")

@servidor_web.route('/', methods=['GET'])
def ruta_principal():
    return jsonify({"servicio": nombre_empresa, "modo": modo_sistema}), 200

@servidor_web.route('/telemetria', methods=['GET'])
def consultar_telemetria():
    lista_diccionarios = [lectura.convertir_a_diccionario() for lectura in historial_lecturas]
    return jsonify(lista_diccionarios), 200

@servidor_web.route('/telemetria', methods=['POST'])
def registrar_telemetria():
    datos_recibidos = request.get_json()

    if not datos_recibidos or 'temperatura' not in datos_recibidos or 'humedad' not in datos_recibidos:
        return jsonify({"error": "Datos incompletos"}), 400

    try:
        nueva_lectura = LecturaSensor(
            identificador_lote=datos_recibidos.get("lote", "LOTE-GENERAL-01"),
            valor_temperatura=datos_recibidos["temperatura"],
            valor_humedad=datos_recibidos["humedad"]
        )
        historial_lecturas.append(nueva_lectura)
        return jsonify({
            "mensaje": "Lectura registrada",
            "datos_guardados": nueva_lectura.convertir_a_diccionario()
        }), 201
    except (ValueError, TypeError):
        return jsonify({"error": "Formato no valido"}), 400

if __name__ == '__main__':
    puerto = int(os.environ.get("PORT", os.environ.get("PUERTO_LOCAL", 5000)))
    servidor_web.run(host='0.0.0.0', port=puerto, debug=True)
