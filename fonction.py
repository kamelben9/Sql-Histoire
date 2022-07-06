<<<<<<< HEAD
import hashlib



#ceci est le fichier pour les fonctions

def verif_user(username, password):


    utilisateur = {"username" : None, "password" : None}

    
    h = hashlib.new('sha256')
    h.update(password.encode())
=======
import crud
import sqlite3
import hashlib
#ceci est le fichier pour les fonctions
# curseur.lastrowid methode qui permet de recuper le dernier element d'une requete SQL


def creation_de_compte():
    utilisateur = {"username" : None , "password" : None}
    input_login = input("Creez un nom d'utilisateur :")
    utilisateur["username"]=input_login
    print(utilisateur["username"])
    input_mot_de_passe = input("Creez un mot de passe :")
    utilisateur["password"]=input_mot_de_passe
    print(utilisateur["password"])

    h = hashlib.new('sha256')
    h.update(input_mot_de_passe.encode())
>>>>>>> 5b8d4e094ab6d5be9a91ba1b7cd51b06bff1bf37

    utilisateur["password"] = h.hexdigest()

    print(utilisateur["password"])
<<<<<<< HEAD
    

    if utilisateur["password"] :
        pass
=======
    crud.ajout_utilisateur(utilisateur["username"],utilisateur["password"])
    

creation_de_compte()
>>>>>>> 5b8d4e094ab6d5be9a91ba1b7cd51b06bff1bf37
