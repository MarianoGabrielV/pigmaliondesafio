
###### ENTREGA DE EXAMEN TECNICO PIGMALION SOFTWARE ######


# Desafio Tecnico - ¿puede un número X formarse usando la suma de 2 elementos de un array?

## Lenguaje a utilizar: Python 

---

## Descripción del problema

Desarrolle (en pseudo código o su lenguaje de preferencia):
1. Un algoritmo que resuelva el problema asumiendo que la máquina en donde va a correrse el
programa tiene recursos infinitos, que el tiempo de ejecución no importa y que lo más
importante es realizar el desarrollo en el menor tiempo posible.
2. Un algoritmo que resuelva el problema asumiendo que los recursos son un bien preciado,
que el tiempo de ejecución si importa y que el tiempo de desarrollo no es importante.
Ante cualquier duda o ambigüedad en el enunciado, es libre de hacer todas las suposiciones
necesarias, siempre y cuando las especifique.


## Ejemplos

    Ejemplo 1
    Input: nums = [1,4,3,9], requiredSum = 8
    Output: False

    Ejemplo 2
    Input: nums = [1,2,4,4], requiredSum = 8
    Output: True


## Se supone lo siguiente:

- Los numeros en la lista son enteros.
- La lista puede contener duplicados.
- El mismo numero no puede sumarse consigo mismo, a menos que aparezca mas de una vez (por ejemplo '[4,4]' lo cual nos llevaria a 4+4=8).
- Si hay multiples pares que sean validos, solamente bastara con detectar uno solo.

---

## Resoluciones

Se opto por el desarrollo de **dos versiones independientes** del algoritmo, siguiendo los lineamientos del ejercicio, estos son los siguientes:



##  Version 1

📄 Archivo: `desafio_pun_uno.py`

- Recorre todos los pares posibles con `doble bucle`.
- Comparación directa entre cada par de elementos.
- ✅ Fácil de implementar.
- ❌ Ineficiente en listas grandes (complejidad **O(n²)**).



## Version 2: Optimizada

📄 Archivo: `desafio_pun_uno.py`

- Recorre la lista una sola vez utilizando un `set`.
- Calcula el complemento necesario en cada paso y verifica si ya apareció.
- ✅ Mucho más eficiente (complejidad **O(n)**).
- ✅ Ideal para listas grandes.

---

## Contexto real de aplicación

Este algoritmo podría utilizarse en sistemas como:

### Control de pagos duplicados en contabilidad
Antes de aprobar una transferencia, verificar si ya existen dos pagos anteriores que suman el mismo monto, para evitar fraudes.



### Juegos o lógica de puntuación
Verificar si dos cartas, fichas o elementos suman un puntaje objetivo.

---

## Ahora, como lo ejecuto?

Desde terminal de su entortno de desarrollo, previamente con Python instalado, ejecutar el siguiente comando:

```bash
python elnombredelarchivo.py
```
---

### Mariano Vergniaud
### FullStack Developer.
### 📧 mariano.unla@gmail.com
### 💼 https://www.linkedin.com/in/marianovergniaud/
