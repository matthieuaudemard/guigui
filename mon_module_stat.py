import statistics as stat
import random as r


def alea(nb, valeur_min=0, valeur_max=100):
    return [r.randint(valeur_min, valeur_max) for _ in range(nb)]


def quartiles(liste):
    return stat.quantiles(liste)
