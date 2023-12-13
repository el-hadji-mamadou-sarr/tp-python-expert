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
def count(word,letter):
    """"
    calculer le nombre de lettres dans un mot 
    """
    return word.count(letter)


def count_letters(word):
    """"
    calcul du nombre d'occurence de chaque lettre dans un mot
    :param word: mot
    :return: dictionnaire de lettres et de leur nombre d'occurence
    """

    # map qui contient les lettres et leur nombre d'occurence
    counts = {}

    # set de lettres dans le mot 
    temp = set(word)
    
    for i in temp:
        counts[i] = word.count(i)
    return counts

# Question 2: Remplacez l'une des lettre qui apparait avec la grande plus fréquence par la lettre e dans le mot m

def replaceLetter(word, new_letter):
    """"
    remplacer la lettre avec la fréqence max par une nouvelle lettre
    :param word: mot
    :param new_letter: nouvelle lettre
    :return: mot avec la lettre remplacée
    """

    # récupération des lettres et de leur nombre d'occurence
    counts = count_letters(word)

    # lettre avec la fréquence max avec laquelle on va remplacer et on a acces
    lettre_max = max(counts, key=counts.get)
    return word.replace(lettre_max, new_letter)


def replaceAllLetters(word, new_letter):
    """"
    remplacer toutes les lettres avec la fréqence max par une nouvelle lettre
    :param word: mot
    :param new_letter: nouvelle lettre
    :return: mot avec la lettre remplacée
    """
    counts = count_letters(word)

    # liste de valeurs de la map counts: que des nombres
    counts_vals = list(counts.values())

    # fréquence max
    _max = max(counts_vals)

    # liste de clés de la map counts avec la fréq max: que des lettres
    list_max = [key for key,val in counts.items() if val==_max]

    # remplacement
    for elt in list_max:
        word = word.replace(elt, new_letter)
    return word

# nbre de "le" et nbre de "e" et effacer les "e"
texte= "Je vois là-bas un être sans tête qui grimpe à une perche sans fin. Tandis que je me promène, tentant de me délasser, d'atteindre ce fond de délassement qu'il est si difficile d'atteindre, qu'il est improbable, quoique ayant tellement soupiré après, que je l'atteigne jamais, tandis que je me promène, je le sais là, je le sens, qui infatigablement (oh non il est terriblement fatigué), qui incessamment grimpe, et s'en va grimpant sur son terrible chemin vertical. Souvent il me paraît comme un amas de loques, où se trahissent deux bras, une sorte de jambe, et ce monstre qui devrait tomber de par sa position même (car elle n'a rien d'une position d'équilibre) et plus encore par l'incessation de son dur exercice, grimpe toujours. Pourtant de cette montée aussi je dois douter, car il échappe assez souvent à mon attention, à cause des soucis de toutes sortes que la vie a toujours su me présenter et je me demande lorsque je le revois, les repères manquant complètement, s'il est plus haut ou, si loin d'avoir accompli des progrès, il ne serait pas plus bas. Parfois je le vois comme un vrai fou, presque sans appui, grotesquement écarté le plus possible de cette perche qu'il hait peut-être et il y aurait de quoi, encore que l'espace lui doive être plus haïssable encore. Henri Michaux"
pronoms = ["le", "la", "les", "l'", "un", "une", "des", "je","tu","il","elle" "nous","vous","ils","de","elles","et", "me","qui","que","quoi","où"]

# Question 3: compter le nombre de fois que vous avez la pronon le, puis le nombre de e, et à l'aide d'un script effacez tous les e.
def delete_letter(word, letter):
    """"
    effacer une lettre dans un mot
    :param word: mot
    :param letter: lettre à effacer
    :return: mot sans la lettre
    """
    return word.replace(letter, '')
    
def counts_nbre_le_and_delete(texte):
    """"
    compter le nombre de 'le', de 'e' et efacer la lettre 'e' dans le texte
    :param texte: texte
    :return: nombre de 'le', de 'e' et texte sans 'e'
    """
    
    return count(texte, "le"),count(texte, "e"), delete_letter(texte, "e")

# Calcul nombre de pronoms
def nombre_pronoms(texte):
    """"
    compter le nombre pronom dans le texte
    :param texte: texte
    :return: nombre de pronom
    """
    nbrePronoms = 0
    # si le pronom est dans le texte, on incrémente le nombre de pronom
    for pronom in pronoms:
        if pronom in texte:
            nbrePronoms +=1
    return nbrePronoms

#Question 4: Suavegarder les statistiques dans    
import json
def saveToJson(texte):
    """"
    enregister le nombre de e et le nombre de pronom dans un fichier json
    :param texte: texte
    """
    path = './stats.json'
    data ={'nombre de e':count(texte, 'e'), 'nombre de pronoms':nombre_pronoms(texte)}
    with open(path, 'w') as file:
        json.dump(data, file)


# question 5: Quel est le mot le plus utilisé dans le texte
def clean_text(texte):
    """"
    nettoyer le texte
    :param texte: texte
    :return: texte nettoyé
    """
    # on nettoie le texte
    texte = texte.replace("'", 'e ')
    texte = texte.replace('.',' ')
    texte = texte.replace(',',' ')
    return texte

def mot_plus_utilise(texte):
    """"
    chercher le mot le plus utilisé
    :param texte: texte
    :return: mot le plus utilisé
    """

    # on nettoie le texte
    texte= clean_text(texte)

    # on récupère les mots dans une liste
    list_mots = texte.split(' ')

    # on compte le nombre d'occurence de chaque mot
    occurence = {}
    for elt in list_mots:
        if elt in occurence:
            occurence[elt]+=1
        else:
            occurence[elt] = 1
    occurence[''] = 0
    return max(occurence, key=occurence.get)

#Question 6: Quel est le mot le plus utilisé dans le texte en dehors des pronoms.
def max_word_sans_pronons(texte):
    """"
    chercher le mot le plus utilisé sans les pronoms
    :param texte: texte
    :return: mot le plus utilisé sans les pronoms
    """

    # on récupre le mot le plus utilisé et si c'est un pronom on le supprime et on reprend
    res = mot_plus_utilise(texte)
    if res in pronoms:
        texte = delete_letter(texte, res)
        res = max_word_sans_pronons(texte)
    return res

suivanteelems = ['a','b','c','a','b','a','d','e']
#Partie 2 Soit la liste, créez des couples de deux valeurs.

def couples(liste):
    """"
    créer des couples de deux valeurs
    :param liste: liste
    :return: couples de deux valeurs
    """
    memo =set()
    couples = []
    j=0
    len_liste = len(liste)
    # on regarde si on a atteint la fin de la liste
    while j<len_liste:
        # si la valeur n'est pas dans le set, on l'ajoute et on parcourt le reste de la liste pour trouver les couples
        if not (liste[j] in memo ):
            memo.add(liste[0])
            # on parcourt le reste de la liste pour trouver les couples
            for i in range(j, len_liste):
                
                if liste[j]  != liste[i] and not (liste[i] in memo):
                    couples.append((liste[j]+ liste[i]))
        j+=1
    return couples
        