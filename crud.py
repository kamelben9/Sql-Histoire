
import sqlite3


def insert_chapter_table(summary):
    connexion = sqlite3.connect("bdd.db")
    curseur = connexion.cursor()
    curseur.execute("INSERT INTO Chapter VALUES( ? , ? ) " , (None , summary))
    connexion.commit()
    connexion.close()

<<<<<<< HEAD
insert_chapter_table("text")
=======
insert_chapter_table("summary")
>>>>>>> 564a461729a82be7aa0de3a6a91d3434536ded0a

def ajout_utilisateur(user_name,password):
    connexion = sqlite3.connect('bdd.db')
    curseur = connexion.cursor()
    curseur.execute("INSERT INTO User  Values (?,?,?);",(None,str(user_name),str(password)))
    connexion.commit()
<<<<<<< HEAD
ajout_utilisateur("test23", "test11")    
=======
>>>>>>> 564a461729a82be7aa0de3a6a91d3434536ded0a


def creer_caracter(prenom, nom, resume):
    connexion = sqlite3.connect("bdd.db")
    curseur = connexion.cursor()
    curseur.execute("INSERT INTO Caracter VALUES (?, ?, ?, ?);", (None, str(prenom), str(nom), str(resume)))
    connexion.commit()
    connexion.close()

<<<<<<< HEAD
creer_caracter("test2", "test3", "test4")


def creer_paragraph(ChapterID, UserID, date, discription):
    connexion = sqlite3.connect("bdd.db")
    curseur = connexion.cursor()
    curseur.execute("INSERT INTO Caracter VALUES (?, ?, ?, ?, ?);", (None, int(ChapterID), UserID, str(date), str(discription)))
    connexion.commit()
    connexion.close()

creer_paragraph("2021", "text text text")
=======
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
>>>>>>> 564a461729a82be7aa0de3a6a91d3434536ded0a
