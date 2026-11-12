from modelo_sensor import LecturaSensor

def ejecutar_pruebas_unitarias():
    lectura_optima = LecturaSensor("LOTE-01", 5.2, 85.0)
    assert lectura_optima.estado_conservacion == "OPTIMO", "Error en rango optimo"

    lectura_calor = LecturaSensor("LOTE-02", 9.1, 78.0)
    assert lectura_calor.estado_conservacion == "ALERTA: RIESGO DE DESCOMPOSICION", "Error alerta calor"

    print("==========================================================")
    print(">>> TODAS LAS PRUEBAS UNITARIAS PASARON EXITOSAMENTE <<<")
    print("==========================================================")

if __name__ == "__main__":
    ejecutar_pruebas_unitarias()
