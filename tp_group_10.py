"""

    Groupe 10
    Paris E4 WMD

    Souleymane FALL
    El Hadji Mamadou Sarr
    Youssouf OUSMANOU OUMAROU
    Khadim Mbacké FALL
    Salamata Nourou MBAYE
"""

m = "Mississippi"

# Question 1 calculez le nombre de i, puis le nombre de chaque lettre
def countI():
    """"
    calcul du nombre de i
    """
    return m.count('i')


def countLettres():
    """"
    calcul du nombre d'occurence de chaque lettre
    """
    counts = {} 
    temp = set(m)
    
    for i in temp:
        counts[i] = m.count(i)
    return counts

# Question 2: Remplacez l'une des lettre qui apparait avec la grande plus fréquence par la lettre e dans le mot m

def replaceLetter(m):
    """"
    remplacer la lettre avec la fréqence max par 'e'
    """
    counts = countLettres()
    lettre_max = max(counts, key=counts.get)
    return m.replace(lettre_max, 'e')


def replaceAllLetters(m):
    
    """"
    remplacer toutes les lettres avec la fréqence max par 'e'
    """

    counts = countLettres()
    counts_vals = list(counts.values())
    _max = max(counts_vals)
    list_max = [key for key,val in counts.items() if val==_max]
    for elt in list_max:
        m = m.replace(elt, 'e')
    return m


# nbre de "le" et nbre de "e" et effacer les "e"
texte= "Je vois là-bas un être sans tête qui grimpe à une perche sans fin. Tandis que je me promène, tentant de me délasser, d'atteindre ce fond de délassement qu'il est si difficile d'atteindre, qu'il est improbable, quoique ayant tellement soupiré après, que je l'atteigne jamais, tandis que je me promène, je le sais là, je le sens, qui infatigablement (oh non il est terriblement fatigué), qui incessamment grimpe, et s'en va grimpant sur son terrible chemin vertical. Souvent il me paraît comme un amas de loques, où se trahissent deux bras, une sorte de jambe, et ce monstre qui devrait tomber de par sa position même (car elle n'a rien d'une position d'équilibre) et plus encore par l'incessation de son dur exercice, grimpe toujours. Pourtant de cette montée aussi je dois douter, car il échappe assez souvent à mon attention, à cause des soucis de toutes sortes que la vie a toujours su me présenter et je me demande lorsque je le revois, les repères manquant complètement, s'il est plus haut ou, si loin d'avoir accompli des progrès, il ne serait pas plus bas. Parfois je le vois comme un vrai fou, presque sans appui, grotesquement écarté le plus possible de cette perche qu'il hait peut-être et il y aurait de quoi, encore que l'espace lui doive être plus haïssable encore. Henri Michaux"
pronoms = ["le", "la", "les", "l'", "un", "une", "des", "je","tu","il","elle" "nous","vous","ils","de","elles","et", "me","qui","que","quoi","où"]

# Question 3: compter le nombre de fois que vous avez la prenon le, puis le nombre de e, et à l'aide d'un script effacez tous les e.
def counts(texte):
    """"
    compter le nombre de 'le', de 'e' et efacer la lettre 'e' dans le texte
    """
    nbre_le = texte.count("le")
    nbre_e = texte.count("e")
    texte = texte.replace('e','')
    return nbre_le, nbre_e, texte

# Calcul nombre de pronoms
def calculPronom():
    """"
    compter le nombre pronom dans le texte
    """
    nbrePronoms = 0
    for pronom in pronoms:
        if pronom in texte:
            nbrePronoms +=1

    return nbrePronoms

#Question 4: Suavegarder les statistiques dans    
import json
def saveToJson():
    """"
    enregister le nombre de e et le nombre de pronom dans un fichier json
    """
    path = './stats.json'
    data ={'nombre de e':texte.count("e"), 'nombre de pronoms':calculPronom()}
    with open(path, 'w') as file:
        json.dump(data, file)


# question 5: Quel est le mot le plus utilisé dans le texte

def motPlusUtilise(texte):
    """"
    chercher le mot le plus utilisé
    """
    list_mots = texte.replace("'", 'e ')
    list_mots = texte.replace('.',' ')
    list_mots = texte.replace(',',' ')
    list_mots = texte.split(' ')

    occurence = {}
    for elt in list_mots:
        if elt in occurence:
            occurence[elt]+=1
        else:
            occurence[elt] = 1
    occurence[''] = 0
    return max(occurence, key=occurence.get)

#Question 6: Quel est le mot le plus utilisé dans le texte en dehors des pronoms.
def max_word_without_pronons(texte):
    """"
    chercher le mot le plus utilisé sans les pronoms
    """
    res = motPlusUtilise(texte)
    while res in pronoms :
        texte = texte.replace(res, '')
        res = motPlusUtilise(texte)
   
    return res



suivanteelems = ['a','b','c','a','b','a','d','e']
#Partie 2 Soit la liste, créez des couples de deux valeurs.

def couples(liste):
    """"
    créer des couples de deux valeurs
    """
    memo =set()
    couples = []
    j=0
    len_liste = len(liste)
    while j<len_liste:
        if not (liste[j] in memo ):
            print(liste[j])
            memo.add(liste[0])
            for i in range(j, len_liste):
                if liste[j]  != liste[i] and not (liste[i] in memo):
                    couples.append((liste[j]+ liste[i]))
        j+=1
    return couples
        
    

print(couples(suivanteelems))