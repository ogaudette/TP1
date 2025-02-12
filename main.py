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
jours_semaine = ["Lundi", "Mardi", "Mercredi", "Jeudi", "Vendredi", "Samedi", "Dimanche"]

amplitude_jours = {jours_semaine[i]: jour[1] - jour[0] for i, jour in enumerate(meteo_semaine)}

print(amplitude_jours)

# 2c
""" Utilisez la notion de compréhension pour obtenir la liste des jours de pluie (pluie > 0) """
jours_de_pluie = {jours for jours in meteo_semaine if jours[2] > 0}
print(jours_de_pluie)

# 2d
""" Utilisez filter pour obtenir les jours où la température max dépasse 25°C """
jours_chauds = set(filter(lambda jour: jour[1] > 25, meteo_semaine))
jours_semaine_chauds = [jours_semaine[i] for i, jour in enumerate(meteo_semaine) if jour in jours_chauds]

print(jours_semaine_chauds)

# 3
""" Une matrice creuse est représentée par un dictionnaire sous la forme {(i,j): valeur} Supposons la 
matrice creuse suivante: matrice = {(0,0): -1, (0,2): 3, (1,1): -2, (2,0): 4, (2,2): 5}"""
matrice = {(0,0): -1, (0,2): 3, (1,1): -2, (2,0): 4, (2,2): 5}

# 3a
""" Utilisez une compréhension de dictionnaire pour créer un nouveau dictionnaire contenant 
uniquement les éléments de la matrice d'origine ayant des valeurs strictement négatives.
"""
matrice_negative = {key: value for key, value in matrice.items() if value < 0}

print(matrice_negative)

# 3b
""" Créez un ensemble (set) contenant les numéros de ligne (i) pour lesquelles il existe au moins une 
valeur non nulle dans la matrice. """
matrice_non_nulle = set(i for i, x in matrice.keys())

print(matrice_non_nulle)

# 3c
"""Utilisez la fonction filter pour obtenir une liste des positions (i, j) dans la matrice où la valeur est 
un nombre impair."""
position_impair = set(filter(lambda i: matrice[i] % 2 != 0, matrice.keys()))
print(position_impair)

# 4
""" Les données des étudiants ont été collectées et regroupées sous la forme suivante: (nom, age, 
(note_math, note_info, note_physique)). Supposons la liste de tuples des étudiants d'une classe 
etudiants = [ ('Alice', 18, (17, 15, 16)), ('Bob', 19, (12, 14, 11)), ('Charlie', 18, (15, 18, 14)), ('David', 20, 
(9, 11, 10))] """
etudiants = [ ('Alice', 18, (17, 15, 16)), ('Bob', 19, (12, 14, 11)), ('Charlie', 18, (15, 18, 14)), ('David', 20,
(9, 11, 10))]

# 4a
""" Créez une fonction lambda qui calcule la moyenne des notes d'un étudiant """
moyenne_notes = lambda etudiant: sum(etudiant[2]) / len(etudiant[2])
print(moyenne_notes(etudiants[2]))

# 4b
""" Utilisez la notion de compréhension pour créer un dictionnaire {nom: moyenne} """
dict_moyenne = {etudiant[0]: sum(etudiant[2]) / len(etudiant[2]) for etudiant in etudiants}
print(dict_moyenne)

# 4c
""" Utilisez filter pour obtenir les étudiants ayant la moyenne en math """
etudiants_pass_math = filter(lambda etudiant: etudiant[2][0] >= 10, etudiants)
nom_pass_math = set(map(lambda etudiant: etudiant[0], etudiants_pass_math))
print(nom_pass_math)
