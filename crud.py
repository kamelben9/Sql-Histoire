
import sqlite3


def insert_chapter_table(summary):
    connexion = sqlite3.connect("bdd.db")
    curseur = connexion.cursor()
    curseur.execute("INSERT INTO Chapter VALUES( ? , ? ) " , (None , summary))
    connexion.commit()
    connexion.close()

insert_chapter_table()

<<<<<<< HEAD
def ajout_utilisateur(user_name,password):
    connexion = sqlite3.connect('bdd.db')
    curseur = connexion.cursor()
    curseur.execute("INSERT INTO User  Values (?,?,?);",(None,str(user_name),str(password)))
    connexion.commit()

def supprime_artiste(id):
    connexion = sqlite3.connect('bdd.db')
    curseur = connexion.cursor()
    curseur.execute("DELETE FROM Artist WHERE userd = ? ;",(id,))
    connexion.commit()

def maj_nom_artiste(id,nom):
    connexion = sqlite3.connect("bdd.db")
    curseur = connexion.cursor()
    curseur.execute("UPDATE Artist SET Name = ? WHERE ArtistId = ? ;",(nom,id))
    connexion.commit()
    connexion.close()

=======


def creer_caracter(prenom, nom, resume):
    connexion = sqlite3.connect("bdd.db")
    curseur = connexion.cursor()
    curseur.execute("INSERT INTO Caracter VALUES (?, ?, ?, ?);", (None, str(prenom), str(nom), str(resume))
    connexion.commit()
    connexion.close()

creer_caracter()
>>>>>>> 89befa2505d96840814147a1e1edd013cd752ac5
