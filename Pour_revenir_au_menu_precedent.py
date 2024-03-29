from re import I
from numpy import kaiser
from sympy import OneMatrix, false, jacobi_normalized, true
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
            return true
        elif(liste[0][2]!=mot_de_passe):
            print("Votre mot de passe n'est pas correct.Essayez encore une fois.")
    else:
        print("Votre identifiant n'existe pas.Essayez encore une fois.")
    
crud.creer_paragraph(15,5,"Test_Marina")

#Cette fonction permet d'afficher le début de l'histroire
def afficher_histoire():
    liste_info = crud.lire_dernier_paragraph()
    print("             Chapitre 1")
    print("Dernier Message : ")

    print("Posté par : "+liste_info[0][0]+" | "+liste_info[0][3])
    print(liste_info[0][4])   

#afficher_histoire()
#Cette fonction permet de lire l'histoire
def lire_histoire(ChapterID):
    liste_histoire =crud.read_chapter(ChapterID)
    print("Ceci est le chapitre "+str(liste_histoire[0][0])+" : (Résumé)")
    print(liste_histoire[0][1])
    print("------------------------------")
    liste_paragraphe=[]
    for i in range(len(liste_histoire)):
        liste_paragraphe.append(liste_histoire[i][2])
    return liste_paragraphe       

#lire_histoire(1)

#Cette fonction permet d'écrire la suite

personne_connecte=identification()
paragraphe_en_cours=1
while(personne_connecte):
    afficher_histoire()

    commande_utilisateur=input("Entrez votre commande : \n (1:Lire Histoire |2: Contester le dernier message | 3:Ecrire la suite | 4 : Se Déconnecter :")
    if(commande_utilisateur=="1"):
        liste_retourne=lire_histoire(1)
        print(liste_retourne)
        i=0
        j=i+3        
        lit_histoire= True

        if len(liste_retourne)>j:
            for _ in liste_retourne[i:j]:
                print(_)
        else:
            for _ in liste_retourne[i:len(liste_retourne)]:
                print(_)
        sous_commande_utilisateur=input("Entrez votre commande : \n (S : Aller à la page suivante |P : Aller à la page précédente | C : Choisir un chapitre | R : Retourner au menu précedent : | K : Lire les commentaires : ")        
        
        if sous_commande_utilisateur=="S":
            if(i+3<len(liste_retourne)):
                i+=3
                if len(liste_retourne)>i+3:                
                    j=i+3
                else:
                    j=len(liste_retourne)
                for _ in liste_retourne[i:j]:
                    print(_)

            while(lit_histoire):
                sous_commande_utilisateur=input("Entrez votre commande : \n (S : Aller à la page suivante |P : Aller à la page précédente | C : Choisir un chapitre | R : Retourner au menu précedent : | K : Lire les commentaires : ")        

                if sous_commande_utilisateur=="S":
                    if(i+3<len(liste_retourne)):
                        i+=3
                        if len(liste_retourne)>i+3:   
                            j=i+3
                        else:
                            j= len(liste_retourne)>j
                        for _ in liste_retourne[i:j]:
                            print(_)
                    else:
                        print("Vous êtes à la dernière page.Il n'y a pas de page suivante.") 
                        if(i+3<len(liste_retourne)):
                            i-=3
                            if len(liste_retourne)>i+3:   
                                j=i+3
                            else:
                                j= len(liste_retourne)>j                        
                        for _ in liste_retourne[i:j]:
                            print(_)
                if sous_commande_utilisateur=="P":
                    if(i-3>=0):
                        i-=3
                        if len(liste_retourne)>i+3:   
                            j=i+3
                        else:
                            j= len(liste_retourne)
                            
                        for _ in liste_retourne[i:j]:
                            print(_)
                    if(0<=i<3):
                        print("Vous êtes à la première page.Vous ne pouvez pas aller en arrière")  
                        if(i-3>=0):
                            i-=3
                            if len(liste_retourne)>i+3:   
                                j=i+3
                            else:
                                j= len(liste_retourne)
                        for _ in liste_retourne[i:j]:
                            print(_)
                    