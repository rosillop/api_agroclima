# Representa la entidad física de una lectura en la cámara de frío

class LecturaSensor:
    def __init__(self, identificador_lote, valor_temperatura, valor_humedad):
        # str(): Función de Python que convierte cualquier dato a texto
        self.identificador_lote = str(identificador_lote)

        # float(): Función de Python que transforma un valor numérico o texto a número decimal
        self.valor_temperatura = float(valor_temperatura)
        self.valor_humedad = float(valor_humedad)

        # Llamamos al método interno para calcular el estado al momento de crear el objeto
        self.estado_conservacion = self.evaluar_cadena_frio()

    def evaluar_cadena_frio(self):
        """Regla de Negocio: Rango seguro para fruta fresca entre 4.0°C y 6.0°C"""
        if self.valor_temperatura > 6.0:
            return "ALERTA: RIESGO DE DESCOMPOSICION"
        elif self.valor_temperatura < 4.0:
            return "ALERTA: RIESGO DE CONGELAMIENTO"
        return "OPTIMO"

    def convertir_a_diccionario(self):
        """Transforma los atributos del objeto a un diccionario estándar de Python"""
        return {
            "identificador_lote": self.identificador_lote,
            "temperatura": self.valor_temperatura,
            "humedad": self.valor_humedad,
            "estado": self.estado_conservacion
        }
