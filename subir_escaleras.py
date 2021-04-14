"""
[Python]
Ejercicio de Subir Escaleras
---------------------------
Autor: Torres Molina Emmanuel Oscar
Version: 1.1
"""

__author__ = "Torres Molina Emmanuel O."
__email__ = "emmaotm@gmail.com"
__version__ = "1.1"



def factorial (num):
    result = 1

    if num > 1:
        result = num * factorial(num-1)

    return result


def cant_posibilidades (n):

    # Lista con la Cantidad de Posibilidades según
    # el nro. de escalón
    posibilidades = []

    # 0 escalones - e0 --> 0 posibilidades
    # 1 escalón - e1 --> 1 posibilidades
    # 2 escalones - e2 --> 2 posibilidades
    e0 = 0
    e1 = 1
    e2 = 2

    if posibilidades == []:
        posibilidades.append(e0)

    else:
        if len(posibilidades) < 4:
            posibilidades.append(e1)
            posibilidades.append(e2)

        else:
            for i in range(len(posibilidades) - 1, n+1):
                e_n = posibilidades[i - 1] + posibilidades[i - 2]
                posibilidades.append(e_n)

    return posibilidades


def total_posibilidades (posibilidades):
    return posibilidades[-1]


if __name__ == "__main__":

    n = 10

    print(cant_posibilidades(n))

    print(total_posibilidades(cant_posibilidades(n)))
