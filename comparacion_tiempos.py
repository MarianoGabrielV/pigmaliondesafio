"""
comparar_tiempos.py

Este programa compara el rendimiento de dos soluciones al mismo problema:
verificar si existe un par de números en una lista que sumen un valor específico.

Se evalúan dos versiones del mismo algoritmo:
1. Versión fuerza bruta (desafio_pun_uno.py)
2. Versión optimizada (desafio_pun_dos.py)

Ambas funciones reciben una lista de números enteros y un número objetivo.
El programa muestra cuánto tarda cada versión en ejecutarse y cuál es más eficiente.
"""

import time
from desafio_pun_uno import existe_una_coincidencia
from desafio_pun_dos import existe_una_coincidencia_optima

def comparar_tiempos():
    print("⏱️ Comparación de tiempos de ejecución entre fuerza bruta y optimizada\n")

    # Creamos una lista de prueba con muchos elementos (del 1 al 5999)
    # Esto permite notar la diferencia entre ambas soluciones
    numeros = list(range(1, 6000))
    
    # Elegimos un número objetivo alto para forzar que el par válido esté al final de la lista
    objetivo = 2000

    # --------------------------
    # Versión 1: Fuerza Bruta
    # --------------------------
    inicio = time.time()  # Guardamos el tiempo inicial
    resultado_bruta = existe_una_coincidencia(numeros, objetivo)
    tiempo_bruta = time.time() - inicio  # Calculamos el tiempo transcurrido
    print(f"Desafío Punto Uno → Resultado: {resultado_bruta} - Tiempo: {tiempo_bruta:.6f} segundos")

    # --------------------------
    # Versión 2: Optimizada
    # --------------------------
    inicio = time.time()
    resultado_optima = existe_una_coincidencia_optima(numeros, objetivo)
    tiempo_optima = time.time() - inicio
    print(f"Desafío Punto Dos (optimizada)   → Resultado: {resultado_optima} - Tiempo: {tiempo_optima:.6f} segundos")

    # --------------------------
    # Resumen Comparativo
    # --------------------------
    diferencia = tiempo_bruta - tiempo_optima
    print("\n📊 En resumen:")
    if tiempo_bruta > tiempo_optima:
        print(f"✅ La versión optimizada fue más rápida por aproximadamente {diferencia:.6f} segundos.")
    else:
        print("❗ Ambas versiones fueron similares en tiempo (lista posiblemente muy pequeña).")

# Punto de entrada del programa
if __name__ == "__main__":
    comparar_tiempos()
