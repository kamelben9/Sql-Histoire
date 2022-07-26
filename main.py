
import crud
import sqlite3
import hashlib
import time
import fonction
from fonction import creation_de_compte


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
            return True,identifiant,liste
        elif(liste[0][2]!=mot_de_passe):
            print("Votre mot de passe n'est pas correct.Essayez encore une fois.")
    else:
        print("Votre identifiant n'existe pas.Essayez encore une fois.")
    
#crud.creer_paragraph(15,5,"Test_Marina")

#Cette fonction permet d'afficher le début de l'histroire
def afficher_histoire():
    liste_info = crud.lire_dernier_paragraph()
    print("             Chapitre "+str(liste_info[0][1]))
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
def ecrire_la_suite():
    liste_caractere=crud.read_chapter_charactere()
    return liste_caractere    

creation_de_compte()
liste_personne_connecte =[]
liste_nom_personne_connecte =[]
liste_identification =identification()
personne_connecte=liste_identification[2][0][0]
nom_utilisateur =liste_identification[1]
liste_personne_connecte.append(liste_identification[2][0][0])
liste_nom_personne_connecte.append(liste_identification[1])
paragraphe_en_cours=1
chapitre_choisi=1
nouvelle_histoire=True
while(personne_connecte):
    afficher_histoire()
    commande_utilisateur=input("""Entrez votre commande : \n (1:Lire Histoire | 2: Contester le dernier message | 3:Ecrire la suite | 4 : Se Déconnecter :""")
    if(commande_utilisateur=="1"):
        lit_histoire=True
        nouvelle_histoire=True
        while(nouvelle_histoire):
            liste_retourne=lire_histoire(chapitre_choisi)       
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
            while(lit_histoire):
                sous_commande_utilisateur=input("Entrez votre commande : \n (S : Aller à la page suivante |P : Aller à la page précédente | C : Choisir un chapitre | R : Retourner au menu précedent : | K : Lire les commentaires : ") 
                
                if sous_commande_utilisateur=="S":
                    if(i+3<len(liste_retourne)):
                        i+=3
                        if len(liste_retourne)>i+3:   
                            j=i+3
                        else:
                            j= len(liste_retourne)
                        for _ in liste_retourne[i:j]:
                            print(_)
                    else:
                        print("Vous êtes à la dernière page.Il n'y a pas de page suivante.") 
                        j= len(liste_retourne)
                        for _ in liste_retourne[i:j]:
                            print(_)
                if sous_commande_utilisateur=="P":
                    if(0<=i<3):
                        print("Vous êtes à la première page.Vous ne pouvez pas aller en arrière")                              
                        if len(liste_retourne)>i+3:   
                            j=i+3
                        else:
                            j= len(liste_retourne)
                            
                        for _ in liste_retourne[i:j]:
                            print(_)
                    else:
                        i-=3
                        if len(liste_retourne)>i+3:   
                            j=i+3
                        else:
                            j= len(liste_retourne)
                        for _ in liste_retourne[i:j]:
                            print(_)

                if sous_commande_utilisateur == "C":
                    nombre_total_chapitre=str(crud.nombre_de_chapitre())
                    print("Il y a "+nombre_total_chapitre)
                    chapitre_choisi=int(input("Entrez le numéro du chapitre que vous voulez voir : "))
                    lit_histoire =False
                    nouvelle_histoire=True
                
                if sous_commande_utilisateur == "R":
                    lit_histoire=False
                    nouvelle_histoire=False
                
                if sous_commande_utilisateur == "K":
                    nombre_total_chapitre=str(crud.nombre_de_chapitre())
                    print("Il y a "+nombre_total_chapitre)
                    chapitre_commentaire_a_voir=str(input("Entrez le numéro du chapitre que vous voulez voir : "))
                    liste_commentaire= crud.lire_commentaire(chapitre_commentaire_a_voir)
                    for i in liste_commentaire:
                        print(i)
    if(commande_utilisateur=="3"):
        liste_info=ecrire_la_suite()
        print("Chapitre "+str(liste_info[0][0])+": (Résumé)")
        print(liste_info[0][1])
        print("----------------")
        print("Liste des personnages : ")
        for i in range(len(liste_info)):
            print(str(liste_info[i][2])+" "+str(liste_info[i][3]))
        print("----------------")
        liste_info_presentation = crud.lire_dernier_paragraph()
        print("Dernier Message : ")
        print("Posté par : "+liste_info_presentation[0][0]+" | "+liste_info_presentation[0][3])

        print("Entrez votre commande")
        commande_caractere=input("""S:Ecrire la suite | R : Retourner au menu précédent | A: ajouter un personnage existant  | C : créer un nouveau personnage : """)
        if(commande_caractere=="S"):
            nouveau_paragraphe = input("Veuillez rentrer votre nouveau paragraphe :")
            nouveau_sommaire = input("Veuillez entrer votre sommaire")
            crud.creer_paragraph(str(liste_info_presentation[0][0]),liste_info_presentation[0][2],nouveau_paragraphe)
            crud.insert_chapter_table(nouveau_sommaire)
        
        if(commande_caractere=="R"):
            lit_histoire=False
            nouvelle_histoire=False

        if(commande_caractere=="A"):
            liste_personnage_existant =crud.afficher_tout_caracter()
            for i in range(len(liste_personnage_existant)):
                print("Voici le nombre du caractere "+str(liste_personnage_existant[i][0])+" pour le caractere "+ str(liste_personnage_existant[i][1])+" "+str(liste_personnage_existant[i][2])+" "+str(liste_personnage_existant[i][3]))
            id_du_caracter=input("Veuillez choisir le nombre pour votre character")
            crud.insert_IsInChapter_table(id_du_caracter,liste_info[0][0])
        if(commande_caractere=="C"):
            prenom_du_caractere=input("Veuillez créer le prénom de votre personnage.")
            nom_du_caractere=input("Veuillez créer le nom de votre personnage")
            description_du_personnage=input("Veuillez décrire votre personnage.")
            crud.creer_caracter(prenom_du_caractere,nom_du_caractere,description_du_personnage)

    if(commande_utilisateur=="2"):
        liste_info_nouvelle =crud.lire_dernier_paragraph()
        print("Ceci est le chapitre "+str(liste_info_nouvelle[0][0])+" : (Résumé)")
        print(liste_info_nouvelle[0][5])
        print("------------------------------")
        print(liste_info_nouvelle[0][1])
        print("Dernier Message : ")

        print("Posté par : "+liste_info_nouvelle[0][0]+" | "+liste_info_nouvelle[0][3])
        print(liste_info_nouvelle[0][4])   
        commande_conteste = input("""Entrer votre commande \n
            C : Contester le dernier paragraphe | R : Retourner au menu précédent """)

        if commande_conteste=="C":
            challenge_verificateur =True
            texte_explicatif=input("Veuillez expliquer pourquoi vous contestez ce paragraphe")
            liste_identifiant = crud.read_user(nom_utilisateur)            
            crud.insert_challenge_table(liste_identifiant[0][0],liste_info_nouvelle[0][6],texte_explicatif)
            while(challenge_verificateur):
                afficher_histoire()
                input_challenge=input("""Entrez votre commande : \n 1:Lire Histoire | 2: Voter pour le challenge |3 : Se Déconnecter : """)
                if input_challenge =="1":
                    lit_histoire_challenge=True
                    nouvelle_histoire_challenge=True
                    while(nouvelle_histoire_challenge):
                        liste_retourne=lire_histoire(chapitre_choisi)       
                        print(liste_retourne)            
                        i=0
                        j=i+3        
                        lit_histoire_challenge= True
                        if len(liste_retourne)>j:
                            for _ in liste_retourne[i:j]:
                                print(_)
                        else:
                            for _ in liste_retourne[i:len(liste_retourne)]:
                                print(_)
                        while(lit_histoire_challenge):
                            sous_commande_utilisateur_challenge=input("Entrez votre commande : \n (S : Aller à la page suivante |P : Aller à la page précédente | C : Choisir un chapitre | R : Retourner au menu précedent : | K : Lire les commentaires : ") 
                            
                            if sous_commande_utilisateur_challenge=="S":
                                if(i+3<len(liste_retourne)):
                                    i+=3
                                    if len(liste_retourne)>i+3:   
                                        j=i+3
                                    else:
                                        j= len(liste_retourne)
                                    for _ in liste_retourne[i:j]:
                                        print(_)
                                else:
                                    print("Vous êtes à la dernière page.Il n'y a pas de page suivante.") 
                                    j= len(liste_retourne)
                                    for _ in liste_retourne[i:j]:
                                        print(_)
                            if sous_commande_utilisateur_challenge=="P":
                                if(0<=i<3):
                                    print("Vous êtes à la première page.Vous ne pouvez pas aller en arrière")                              
                                    if len(liste_retourne)>i+3:   
                                        j=i+3
                                    else:
                                        j= len(liste_retourne)
                                        
                                    for _ in liste_retourne[i:j]:
                                        print(_)
                                else:
                                    i-=3
                                    if len(liste_retourne)>i+3:   
                                        j=i+3
                                    else:
                                        j= len(liste_retourne)
                                    for _ in liste_retourne[i:j]:
                                        print(_)

                            if sous_commande_utilisateur_challenge == "C":
                                nombre_total_chapitre_challenge=str(crud.nombre_de_chapitre())
                                print("Il y a "+nombre_total_chapitre)
                                chapitre_choisi=int(input("Entrez le numéro du chapitre que vous voulez voir : "))
                                lit_histoire_challenge =False
                                nouvelle_histoire_challenge=True
                            
                            if sous_commande_utilisateur_challenge == "R":
                                lit_histoire_challenge=False
                                nouvelle_histoire_challenge=False
                            
                            if sous_commande_utilisateur_challenge == "K":
                                nombre_total_chapitre=str(crud.nombre_de_chapitre())
                                print("Il y a "+nombre_total_chapitre)
                                chapitre_commentaire_a_voir=str(input("Entrez le numéro du chapitre que vous voulez voir : "))
                                liste_commentaire= crud.lire_commentaire(chapitre_commentaire_a_voir)
                                for i in liste_commentaire:
                                    print(i)
                if input_challenge=="2":
                    #recuperer id personne_connecte
                    ################################
                    personnes_ayant_votés=0
                    resultat_vote=0
                    liste_des_votants = liste_personne_connecte.copy()
                    liste_nom_des_votant =liste_nom_personne_connecte.copy()
                    nombre_de_votants=len(liste_des_votants)
                    while(personnes_ayant_votés<nombre_de_votants):
                        while(len(liste_des_votants)!=0):
                            verification_id =liste_identification[2][0][0]
                            verification_username =liste_identification[2][0][1]
                            for _ in liste_des_votants:
                                if verification_id == _ :
                                    vote_input =int(input("Voter 1 pour garder ce paragraphe | Voter 2 pour le supprimmer"))
                                    liste_participant=crud.read_user(verification_username)
                                    if vote_input == 1:
                                        resultat_vote +=1
                                    if vote_input == 2:
                                        resultat_vote -=1
                                    personnes_ayant_votés +=1
                                liste_des_votants.remove(verification_id)
                                liste_nom_des_votant.remove(verification_username)
                                
                    ################################
                    liste_info_challenge =crud.lire_dernier_paragraph()
                    texte_defier=liste_info_challenge[0][4]

                    fonction.vote(liste_info_challenge[0][6],resultat_vote)
                    if resultat_vote >=0:
                        print("On garde le dernier paragraphe.")
                        challenge_verificateur =False
                    else:
                        crud.supprime_paragraphe(liste_info_challenge[0][6])
                        print("On a supprimé le dernier paragraphe, vous pouvez reprendre l'écriture.")
                        challenge_verificateur =False
                if input_challenge =="4":
                    quit()
                    #On peut sinon faire
                    #personne_connecte = False    
        if commande_conteste=="R":
            lit_histoire_challenge=False
            nouvelle_histoire_challenge=False
    
    if(commande_utilisateur=="4"):
        quit()
        #On peut sinon faire
        #personne_connecte = False
