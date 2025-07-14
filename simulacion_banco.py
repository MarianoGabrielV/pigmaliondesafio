from desafio_pun_dos import existe_una_coincidencia_optima

# Opcional: formato de salida con colores
def mostrar_resultado(mensaje, es_exito=True):
    COLOR_VERDE = "\033[92m"
    COLOR_ROJO = "\033[91m"
    RESET = "\033[0m"
    color = COLOR_VERDE if es_exito else COLOR_ROJO
    print(f"{color}{mensaje}{RESET}")

def simular_banco():
    print("🏦 Simulación del Sistema de Validación Bancaria")
    print("-------------------------------------------------")
    print("Objetivo: Verificar si una nueva transferencia ya fue cubierta por dos anteriores.\n")

    # Transferencias previas registradas
    transferencias_previas = [1200, 3500, 1800, 2200,4000]
    
    # Monto de nueva transferencia a validar
    nuevo_monto = 5000

    # Mostrar datos
    print(f"🔢 Transferencias anteriores registradas: {transferencias_previas}")
    print(f"💰 Monto de nueva transferencia solicitada: {nuevo_monto}\n")

    # Aplicar algoritmo optimizado
    if existe_una_coincidencia_optima(transferencias_previas, nuevo_monto):
        mostrar_resultado("⚠️ Alerta: ya existen dos transferencias que suman ese monto. Revisión manual sugerida.", es_exito=False)
    else:
        mostrar_resultado("✅ La transferencia es válida. No se detectan duplicaciones.", es_exito=True)

if __name__ == "__main__":
    simular_banco()
