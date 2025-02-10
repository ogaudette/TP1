# Gaudette, Olivier
# DA : 6331477
# TP-01 2025-02-05

"""Créez une fonction racines_communes qui prend deux ensembles de nombres représentant les
racines de deux polynômes et retourne :
• l'ensemble des racines qui ne sont pas communes aux deux ensembles
• l'ensemble des racines des deux ensembles
• l'ensemble des racines paires qui sont communes aux deux ensembles"""


# 1
def racines_communes(rac_poly1, rac_poly2):
    communes_ensemble = rac_poly1.symetric_difference(rac_poly2)
    deux_ensembles = rac_poly1.union(rac_poly2)
    pairs = {x for x in rac_poly1.intersection(rac_poly2) if x % 2 == 0}
    return communes_ensemble, deux_ensembles, pairs


# 2
"""Supposons les données météo journalières suivantes sous forme de tuples (temp_min, 
temp_max, pluie) meteo_semaine = [ (12, 25, 0), (15, 28, 10), (14, 27, 5), (13, 24, 15), (11, 22, 8), (10, 
20, 20), (12, 23, 0)]"""

meteo_semaine = [(12, 25, 0), (15, 28, 10), (14, 27, 5), (13, 24, 15), (11, 22, 8), (10,
                                                                                     20, 20), (12, 23, 0)]

# 2a
"""Créez une fonction lambda qui calcule l'amplitude thermique journalière. Pour un tuple de 
données météo journalier (temp_min, temp_max, pluie), il va retourner l'amplitude thermique 
du jour."""

amplitude_thermique = lambda meteo_semaine: meteo_semaine[1] - meteo_semaine[0]

print(amplitude_thermique(meteo_semaine[5]))

#2b
""" Créez un dictionnaire associant chaque jour à son amplitude thermique """
jours = ["Lundi", "Mardi", "Mercredi", "Jeudi", "Vendredi", "Samedi", "Dimanche"]

# FIX ME
amplitude_jours = {jours: amplitude_thermique(meteo_semaine) for jours, meteo_semaine
                   in enumerate(meteo_semaine)}
print(amplitude_jours)

# 2c
""" Utilisez la notion de compréhension pour obtenir la liste des jours de pluie (pluie > 0) """
# FIX ME
pluie = {jours_pluie: True if meteo_semaine[2] > 0 else False for jours_pluie, meteo in meteo_semaine.items()}
print(pluie)

# 2d
""" Utilisez filter pour obtenir les jours où la température max dépasse 25°C """

