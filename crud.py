
import sqlite3


def insert_chapter_table(summary):
    connexion = sqlite3.connect("bdd.db")
    curseur = connexion.cursor()
    curseur.execute("INSERT INTO Chapter VALUES( ? , ? ) " , (None , summary))
    connexion.commit()
    connexion.close()

insert_chapter_table("summary")

def ajout_utilisateur(user_name,password):
    connexion = sqlite3.connect('bdd.db')
    curseur = connexion.cursor()
    curseur.execute("INSERT INTO User  Values (?,?,?);",(None,str(user_name),str(password)))
    connexion.commit()


def creer_caracter(prenom, nom, resume):
    connexion = sqlite3.connect("bdd.db")
    curseur = connexion.cursor()
    curseur.execute("INSERT INTO Caracter VALUES (?, ?, ?, ?);", (None, str(prenom), str(nom), str(resume)))
    connexion.commit()
    connexion.close()

creer_caracter("test","test","test")

def insert_IsInChapter_table(ChapterId,CaracterId):
    connexion = sqlite3.connect("bdd.db")
    curseur = connexion.cursor()
    curseur.execute("INSERT INTO IsInChapter VALUES( ? , ? ) " , (None , None))
    connexion.commit()
    connexion.close()

insert_IsInChapter_table(1,1)



def insert_challenge_table(UserId, ParagraphId, str, int):
    connexion = sqlite3.connect("bdd.db")
    curseur = connexion.cursor()
    curseur.execute("INSERT INTO Challenge VALUES( ? , ? , ?, ?) " , (None , None, str, int))
    connexion.commit()
    connexion.close()

insert_challenge_table(1,1,"toto",8)