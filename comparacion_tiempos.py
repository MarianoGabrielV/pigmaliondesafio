import time
from desafio_pun_uno import existe_una_coincidencia
from desafio_pun_dos import existe_una_coincidencia_optima

def comparar_versiones():
    print("⏱️ Comparación de tiempos de ejecución entre fuerza bruta y optimizada\n")

    # Lista de prueba suficientemente grande para notar diferencia
    numeros = list(range(1, 5000))  # podés aumentar este número si tu PC lo soporta bien
    objetivo = 9998  # Solo el último par suma esto

    # Versión 1: Fuerza bruta
    inicio = time.time()
    resultado_bruta = existe_una_coincidencia(numeros, objetivo)
    tiempo_bruta = time.time() - inicio
    print(f"🧪 Fuerza bruta     → Resultado: {resultado_bruta} - Tiempo: {tiempo_bruta:.6f} segundos")

    # Versión 2: Optimizada
    inicio = time.time()
    resultado_optimizada = existe_una_coincidencia_optima(numeros, objetivo)
    tiempo_optimizada = time.time() - inicio
    print(f"⚡ Versión optimizada → Resultado: {resultado_optimizada} - Tiempo: {tiempo_optimizada:.6f} segundos")

    # Resumen
    diferencia = tiempo_bruta - tiempo_optimizada
    print("\n📊 Resumen:")
    if tiempo_bruta > tiempo_optimizada:
        print(f"La versión optimizada fue más rápida por aproximadamente {diferencia:.6f} segundos.")
    else:
        print("Ambas versiones fueron similares en tiempo (probablemente la lista es pequeña).")

if __name__ == "__main__":
    comparar_versiones()
