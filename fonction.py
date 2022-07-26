import crud
import sqlite3
import hashlib
#ceci est le fichier pour les fonctions
# curseur.lastrowid methode qui permet de recuper le dernier element d'une requete SQL



def creation_de_compte():
    demande_inscription = input("Voulez vous créez un compte ?  \n Taper Y pour oui | Taper N pour non : ")
    if demande_inscription=="N":
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
        
        crud.ajout_utilisateur(utilisateur["username"],utilisateur["password"])
    else :
        pass

def vote(paragraph_id, vote):

    connexion = sqlite3.connect("bdd.db")
    curseur = connexion.cursor()
    curseur.execute("""SELECT * FROM Challenge
                        WHERE ParagraphID = ?""",(str(paragraph_id),))

    vote_actuel = curseur.fetchone()[3]
    vote_final =str(int(vote)+int(vote_actuel))

    curseur.execute("""UPDATE Challenge SET Vote = ?
                        WHERE ParagraphID = ?""",(vote_final,str(paragraph_id)))
    connexion.commit()
    connexion.close()