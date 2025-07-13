# par_suma_optimizado.py

def existe_par_con_suma_optimizado(lista_numeros, suma_objetivo):
    """
    Versión 2: Optimizada
    Busca si existe un par de números que sumen el objetivo.
    Utiliza un conjunto para reducir la complejidad a O(n).

    :param lista_numeros: Lista de números enteros
    :param suma_objetivo: Valor objetivo a alcanzar con la suma de dos elementos
    :return: True si existe un par con esa suma, False en caso contrario
    """
    numeros_vistos = set()
    for numero_actual in lista_numeros:
        numero_necesario = suma_objetivo - numero_actual
        if numero_necesario in numeros_vistos:
            return True
        numeros_vistos.add(numero_actual)
    return False


if __name__ == "__main__":
    numeros_ejemplo = [1, 4, 3, 9]
    objetivo = 8
    print(existe_par_con_suma_optimizado(numeros_ejemplo, objetivo))  # Esperado: False

    numeros_ejemplo = [1, 2, 4, 4]
    objetivo = 8
    print(existe_par_con_suma_optimizado(numeros_ejemplo, objetivo))  # Esperado: True
