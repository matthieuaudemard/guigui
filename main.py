import mon_module_stat as stat

nombre = int(input("Nombre de valeurs souhaitées : "))
while nombre <= 0:
    nombre = int(input("Nombre incorrect ! Nombre de valeurs souhaitées : "))

liste = stat.alea(nombre, valeur_max=1000)

q1, med, q3 = stat.quartiles(liste)

print("1er quartile :", q1)
print("Médiane :", med)
print("3eme quartile :", q3)
