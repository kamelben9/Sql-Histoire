import hashlib

from sympy import re
import crud
import sqlite3
from datetime import datetime


#ceci est le fichier pour les fonctions
# curseur.lastrowid methode qui permet de recuper le dernier element d'une requete SQL
"""

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

    utilisateur["password"] = h.hexdigest()

    print(utilisateur["password"])
    

    if utilisateur["password"] :
        pass
    crud.ajout_utilisateur(utilisateur["username"],utilisateur["password"])
"""
#creation_de_compte()

def afficher_infos(username, datetime):


    connexion = sqlite3.connect("bdd.db")
    curseur = connexion.cursor()
    curseur.execute("SELECT * FROM User WHERE Username = ? ",(username,(str(datetime.now()))))
    return curseur.fetchall()

    listinfo = crud.read_paragraph()
