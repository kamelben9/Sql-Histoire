import crud
import sqlite3
import hashlib
from crud import read_user
#ceci est le fichier pour les fonctions
# curseur.lastrowid methode qui permet de recuper le dernier element d'une requete SQL



def creation_de_compte():
    demande_creation_compte=int(input("Voulez vous créer un compte ? \n 1:Oui | 2: Non : "))
    if demande_creation_compte == 1 :
        veut_creer_compte=True
        while veut_creer_compte:
            est_present = True        
            
            while est_present:
                utilisateur = {"username" : None , "password" : None}
                input_login = input("Creez un nom d'utilisateur ou Taper A pour Sortir :")
                if input_login=="A":
                    veut_creer_compte=False
                    input_login=""
                    
                liste_verification_login =read_user(input_login)
                if liste_verification_login != []:
                    print("Le nom est déja utilisé")
                else:
                    est_present=False
                    utilisateur["username"]=input_login
                    input_mot_de_passe = input("Creez un mot de passe ou Taper A pour Sortir :")

                    if input_mot_de_passe=="A":
                        veut_creer_compte=False
                        input_mot_de_passe=""
                
                    utilisateur["password"]=input_mot_de_passe
                    print(utilisateur["password"])
                    h = hashlib.new('sha256')
                    h.update(input_mot_de_passe.encode())
                    utilisateur["password"] = h.hexdigest()
                    veut_creer_compte=False
        if(utilisateur["username"]!="" and utilisateur["password"]!=""):
            crud.ajout_utilisateur(utilisateur["username"],utilisateur["password"])

def vote(paragraph_id, vote):

    connexion = sqlite3.connect("bdd.db")
    curseur = connexion.cursor()
    curseur.execute("""SELECT * FROM Challenge
                        WHERE ParagraphID = ?""",(paragraph_id))

    vote_actuel = curseur.fetchone()[3]
    curseur.execute("""UPDATE * FROM Challenge
                        WHERE ParagraphID = ?""",(vote_actuel + vote,paragraph_id))
    connexion.commit()
    connexion.close()