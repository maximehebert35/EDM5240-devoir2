# coding: utf-8

import csv
fichier1 = "concordia1.csv"
f1 = open(fichier1)
devoir = csv.reader(f1)

# Nombre de caractères dans les titres
longTitre = len(devoir[2])
print(longTitre)

# Maîtrise ou doctorat
for these in devoir:
	if "M." in devoir[6]:
		these = "maîtrise"
	else:
		these = "doctorat"
	print(these)
