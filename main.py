import random as r

cle_chiffrement = ["a","z","e","r","t","y","u","i","o","p","q","s","d","f","g","h","j","k","l","m","w","x","c","v","b","n"]

def decalage(lettre, nb_decalage):
    if lettre in cle_chiffrement:
        index = cle_chiffrement.index(lettre)
        index_decale = (index + nb_decalage) % len(cle_chiffrement)
        return cle_chiffrement[index_decale]
    else:
        return lettre

def chiffrement(phrase):
    phrase_chiffree = ""
    for index, lettre in enumerate(phrase):
        if lettre not in cle_chiffrement:
            phrase_chiffree += lettre
        elif index % 4 == 0:
            phrase_chiffree+=decalage(lettre, 2)
        elif index % 2 == 0:
            phrase_chiffree+=decalage(lettre, 1)
        elif index % 2 != 0 and index % 3 == 0:
            phrase_chiffree+=decalage(lettre, -2)
        elif index % 2 != 0 and index % 3 != 0:
            phrase_chiffree+=decalage(lettre, -1)
        else:
            phrase_chiffree+=lettre
    return phrase_chiffree

def dechiffrement(phrase):
    phrase_dechiffree = ""
    for index, lettre in enumerate(phrase):
        if lettre not in cle_chiffrement:
            phrase_dechiffree += lettre
        elif index % 4 == 0:
            phrase_dechiffree+=decalage(lettre, -2)
        elif index % 2 == 0:
            phrase_dechiffree+=decalage(lettre, -1)
        elif index % 2 != 0 and index % 3 == 0:
            phrase_dechiffree+=decalage(lettre, 2)
        elif index % 2 != 0 and index % 3 != 0:
            phrase_dechiffree+=decalage(lettre, 1)
        else:
            phrase_dechiffree+=lettre
    return phrase_dechiffree

chiffrement_ou_dechiffrement = input("Voulez-vous chiffrer ou déchiffrer une phrase ? (c/d) : ").lower()

if chiffrement_ou_dechiffrement == "c":
    phrase_a_chiffrer = input("Entrez la phrase à chiffrer : ").lower()
    print("La phrase chiffrée est : ", chiffrement(phrase_a_chiffrer))
elif chiffrement_ou_dechiffrement == "d":
    phrase_a_dechiffrer = input("Entrez la phrase à déchiffrer : ").lower()
    print("La phrase déchiffrée est : ", dechiffrement(phrase_a_dechiffrer))  