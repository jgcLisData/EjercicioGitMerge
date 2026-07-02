import random

from astronomia.aliens import aliens
from astronomia.planetas import planetas
from astronomia.galaxias import galaxias

def explora(a):
    sitios_a_explorar = ["rio", "lago", "campo"]
    print(f"el alien {a} explora {random.choice(sitios_a_explorar)}")

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
