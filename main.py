import random

from astronomia.aliens import aliens
from astronomia.planetas import planetas
from astronomia.galaxias import galaxias


def explora(a):
    sitios_a_no_explorar = ["los baños", "el granero", "la madriguera"]
    print(f"el alien {a} no va a explorar {random.choice(sitios_a_no_explorar)}")


def cosmos(a, p, g):
    for alien in a:
        print(
            f"El {alien} del planeta {random.choce(p)} de la galaxia {random.choice(g)}"
        )
        explora(a)


"""
Rutina/Funcion principal
"""
if __name__ == "__main__":
    cosmos(aliens, planetas, galaxias)
