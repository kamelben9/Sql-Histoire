
import sqlite3


def insert_chapter_table(summary):
    connexion = sqlite3.connect("bdd.db")
    curseur = connexion.cursor()
    curseur.execute("INSERT INTO Chapter VALUES( ? , ? ) " , (None , summary))
    connexion.commit()
    connexion.close()

insert_chapter_table("text")

def ajout_utilisateur(user_name,password):
    connexion = sqlite3.connect('bdd.db')
    curseur = connexion.cursor()
    curseur.execute("INSERT INTO User  Values (?,?,?);",(None,str(user_name),str(password)))
    connexion.commit()
ajout_utilisateur("test23", "test11")    


def creer_caracter(prenom, nom, resume):
    connexion = sqlite3.connect("bdd.db")
    curseur = connexion.cursor()
    curseur.execute("INSERT INTO Caracter VALUES (?, ?, ?, ?);", (None, str(prenom), str(nom), str(resume)))
    connexion.commit()
    connexion.close()

creer_caracter("test2", "test3", "test4")


def creer_paragraph(ChapterID, UserID, date, discription):
    connexion = sqlite3.connect("bdd.db")
    curseur = connexion.cursor()
    curseur.execute("INSERT INTO Caracter VALUES (?, ?, ?, ?, ?);", (None, int(ChapterID), UserID, str(date), str(discription)))
    connexion.commit()
    connexion.close()

creer_paragraph("2021", "text text text")