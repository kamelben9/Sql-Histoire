
import sqlite3


def insert_chapter_table(summary):
    connexion = sqlite3.connect("bdd.db")
    curseur = connexion.cursor()
    curseur.execute("INSERT INTO Chapter VALUES( ? , ? ) " , (None , summary))
    connexion.commit()
    connexion.close()

insert_chapter_table("Test")

#partie utilisateur crud

insert_chapter_table("text")
insert_chapter_table("summary")

def ajout_utilisateur(user_name,password):
    connexion = sqlite3.connect('bdd.db')
    curseur = connexion.cursor()
    curseur.execute("INSERT INTO User  Values (?,?,?);",(None,str(user_name),str(password)))
    connexion.commit()
ajout_utilisateur("test23", "test11")    




def supprime_utilisateur(id):
    connexion = sqlite3.connect('bdd.db')
    curseur = connexion.cursor()
    curseur.execute("DELETE FROM User WHERE userID = ? ;",(id,))
    connexion.commit()

def maj_nom_utilisateur(id,nom):
    connexion = sqlite3.connect("bdd.db")
    curseur = connexion.cursor()
    curseur.execute("UPDATE User SET Name = ? WHERE UserID = ? ;",(nom,id))
    connexion.commit()
    connexion.close()

def maj_password_utilisateur(id,nom):
    connexion = sqlite3.connect("bdd.db")
    curseur = connexion.cursor()
    curseur.execute("UPDATE User SET Name = ? WHERE UserID = ? ;",(nom,id))
    connexion.commit()
    connexion.close()



def creer_caracter(prenom, nom, resume):
    connexion = sqlite3.connect("bdd.db")
    curseur = connexion.cursor()
    curseur.execute("INSERT INTO Caracter VALUES (?, ?, ?, ?);", (None, str(prenom), str(nom), str(resume)))
    connexion.commit()
    connexion.close()

#Creer méthode crud pour commentaire
def ajout_commentaire(user_id,chapter_id,date,text):
    connexion = sqlite3.connect('bdd.db')
    curseur = connexion.cursor()
    curseur.execute("INSERT INTO Comment  Values (?,?,?,?,?);",(None,user_id,chapter_id,date,text))
    connexion.commit()
ajout_commentaire(1,1,1,"tester")
def supprime_commentaire(id):
    connexion = sqlite3.connect('bdd.db')
    curseur = connexion.cursor()
    curseur.execute("DELETE FROM Comment WHERE CommentID = ? ;",(id,))
    connexion.commit()
def maj_commentaire(id,text_commentaire):
    connexion = sqlite3.connect("bdd.db")
    curseur = connexion.cursor()
    curseur.execute("UPDATE Comment SET text = ? WHERE CommentID = ? ;",(text_commentaire,id))
    connexion.commit()
    connexion.close()

supprime_commentaire(2)
maj_commentaire(3,"test_modifier")
creer_caracter("test","test","test")

creer_caracter("test2", "test3", "test4")


def creer_paragraph(ChapterID, UserID, date, discription):
    connexion = sqlite3.connect("bdd.db")
    curseur = connexion.cursor()
    curseur.execute("INSERT INTO Caracter VALUES (?, ?, ?, ?, ?);", (None, int(ChapterID), UserID, str(date), str(discription)))
    connexion.commit()
    connexion.close()

creer_paragraph("2021", "text text text")

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

