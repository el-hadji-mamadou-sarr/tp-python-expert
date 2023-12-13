def mots(chaine):
    nbr_de_i = chaine.count('i')

    nbr = {}
    for letter in chaine:
        if letter in nbr:
            nbr[letter] += 1
        else:
            nbr[letter] = 1

# Remplacement de la lettre la plus fréquente par 'e'
    lettre_max = max(nbr, key=nbr.get)
    nouvelle_chaine = chaine.replace(lettre_max, 'e')
    
    return nbr_de_i, nbr, nouvelle_chaine

m = "Mississippi"
resultat = mots(m)

# Affichage des résultats
nbr_de_i, nbr, nouvelle_chaine = resultat
print(f"Nombre de i : {nbr_de_i}")
print("Fréquence d'apparition de chaque lettre dans la chaîne 😊")
for letter, occ in nbr.items():
    print(f"{letter}: {occ}")
print(f"Chaine après remplacement: {nouvelle_chaine}")