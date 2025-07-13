# existe_una_coincidencia_optima

"""
    Version 2: Optimizada
    Verifica si existe al menos un par de numeros en la lista cuya suma sea igual al numero solicitado.
    Utiliza un conjunto para guardar los numeros ya analizados.
    Asi, en lugar de revisar todos los pares posibles uno por uno, el algoritmo puede encontrar rápidamente si existe un numero que complete la suma deseada.
    Esto permite resolver el problema mucho mas rapido, incluso cuando la lista es muy larga.

    Parametros:
    lista_numeros: Lista de numeros enteros
    suma_a_llegar: Numero que se desea alcanzar sumando dos elementos de la lista
    True: Si existe al menos un par con esa suma.
    False: En caso contrario.
"""

def existe_una_coincidencia_optima(lista_numeros, suma_a_llegar):
    numeros_vistos = set()  # Conjunto para guardar los números ya analizados

    for numero_actual in lista_numeros:
        numero_faltante = suma_a_llegar - numero_actual  # Calculamos cuanto falta para llegar a la suma objetivo

        if numero_faltante in numeros_vistos:
            # Si el numero que falta ya fue visto anteriormente, existe una coincidencia
            return True

        # Si no se encontró aun el número complementario, guardamos el actual para futuras comparaciones
        numeros_vistos.add(numero_actual)

    # Si se recorrio toda la lista sin encontrar ningún par que sume el objetivo
    return False


# Ejemplos de uso para verificar el correcto funcionamiento
if __name__ == "__main__":
    numeros_ejemplo = [1, 4, 3, 9]
    objetivo = 8
    print(existe_una_coincidencia_optima(numeros_ejemplo, objetivo))  # Esperado: False

    numeros_ejemplo = [4, 2, 1, 4]
    objetivo = 8
    print(existe_una_coincidencia_optima(numeros_ejemplo, objetivo))  # Esperado: True
