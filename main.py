import crud
import sqlite3
import hashlib
import time


#Motde passe identification, et affichage debut
def identification():
    identifiant= input("Entrez votre login : ")
    liste = crud.read_user(identifiant)
    print(liste)    
    mot_de_passe=input("Entrez votre mot_de_passe : ")
    h = hashlib.new('sha256')
    h.update(mot_de_passe.encode())

    mot_de_passe = h.hexdigest()
    if(liste != []):
        if(liste[0][1]==identifiant and liste[0][2]==mot_de_passe):
            print("Bienvenue dans Maoka , "+identifiant+" !")
        elif(liste[0][2]!=mot_de_passe):
            print("Votre mot de passe n'est pas correct.Essayez encore une fois.")
    else:
        print("Votre identifiant n'existe pas.Essayez encore une fois.")

crud.creer_paragraph(15,5,"Test_Marina")

#Cette fonction permet d'afficher le début de l'histroire
def afficher_histoire():
    liste_info = crud.lire_dernier_paragraph()


    print("Dernier Message : ")

    print("Posté par : "+liste_info[0][0]+" | "+liste_info[0][3])
    print(liste_info[0][4])   

#afficher_histoire()

#Cette fonction permet de lire l'histoire
def lire_histoire(userID):
    liste_histoire =crud.read_chapter(userID)
    print("Ceci est le chapitre "+str(liste_histoire[0][0])+" : (Résumé)")
    print(liste_histoire[0][1])
    print("------------------------------")
    for i in range(len(liste_histoire)):
        print(liste_histoire[i][2])
#lire_histoire(1)

#Cette fonction permet d'écrire la suite


