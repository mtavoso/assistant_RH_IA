import numpy as np

def intersection_montante_descendante(a1, a2, b1, b2):
    """Calcule le degré d'intersection entre deux segments flous."""

    if a1 == a2:
        x = a2
        return (b2 - x) / (b2 - b1)

    elif b1 == b2:
        x = b2
        return (x - a1) / (a2 - a1)

    x = (b2 + a1 * (b2 - b1) / (a2 - a1)) / (1 + (b2 - b1) / (a2 - a1))
    return (b2 - x) / (b2 - b1)


def degre_appartenance(x_tri, mf_list):

    """
    Calcule les degrés d'appartenance d'une valeur triangulaire/trapézoïdale
    """
    a1, a2, a3 = x_tri
    liste_y = []

    for mf in mf_list:
        param = mf.Parameters

        if mf.Type == "trimf":
            b1, b2, b3 = param

            if a1 >= b3 or a3 <= b1:
                y = 0

            elif a1 <= b3 and a2 >= b2:
                y = intersection_montante_descendante(a1, a2, b2, b3)

            elif a3 >= b1 and a2 <= b2:
                y = intersection_montante_descendante(b1, b2, a2, a3)

            else:
                y = 1  # cas recouvrement fort

        elif mf.Type == "trapmf":
            b1, b2, b3, b4 = param

            if a1 >= b4 or a3 <= b1:
                y = 0

            elif a1 <= b4 and a2 >= b3:
                y = intersection_montante_descendante(a1, a2, b3, b4)

            elif a3 >= b1 and a2 <= b2:
                y = intersection_montante_descendante(b1, b2, a2, a3)

            elif b2 < a2 < b3:
                y = 1
            else:
                y = 0

        liste_y.append(y)

    return np.array(liste_y)