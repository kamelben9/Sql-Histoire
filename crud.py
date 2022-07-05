
import sqlite3


def insert_chapter_table(summary):
    connexion = sqlite3.connect("bdd.db")
    curseur = connexion.cursor()
    curseur.execute("INSERT INTO Chapter VALUES( ? , ? ) " , (None , summary))
    connexion.commit()
    connexion.close()

insert_chapter_table()



def creer_caracter(prenom, nom, resume):
    connexion = sqlite3.connect("bdd.db")
    curseur = connexion.cursor()
    curseur.execute("INSERT INTO Caracter VALUES (?, ?, ?, ?);", (None, str(prenom), str(nom), str(resume))
    connexion.commit()
    connexion.close()

creer_caracter()