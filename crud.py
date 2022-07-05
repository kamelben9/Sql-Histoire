
import sqlite3
from datetime import datetime

#Creation des fonctions (create)

def ajout_utilisateur(user_name,password):
    connexion = sqlite3.connect('bdd.db')
    curseur = connexion.cursor()
    curseur.execute("INSERT INTO User  Values (?,?,?);",(None,str(user_name),str(password)))
    connexion.commit()
#ajout_utilisateur()  

def insert_challenge_table(UserId, ParagraphId, text, vote):
    connexion = sqlite3.connect("bdd.db")
    curseur = connexion.cursor()
    curseur.execute("INSERT INTO Challenge VALUES( ? , ? , ?, ?) " , (UserId , ParagraphId, str(text), int(vote)))
    connexion.commit()
    connexion.close()

insert_challenge_table(1,1,"toto",8)

def creer_paragraph(ChapterID, UserID, description):
    connexion = sqlite3.connect("bdd.db")
    curseur = connexion.cursor()
    curseur.execute("INSERT INTO Paragraph VALUES (?, ?, ?, ?, ?);", (None, ChapterID, UserID, str(datetime.now()), str(description)))
    connexion.commit()
    connexion.close()

creer_paragraph(1,1,"toto")


def ajout_commentaire(user_id,chapter_id,date,text):
    connexion = sqlite3.connect('bdd.db')
    curseur = connexion.cursor()
    curseur.execute("INSERT INTO Comment  Values (?,?,?,?,?);",(None,user_id,chapter_id,date,text))
    connexion.commit()
ajout_commentaire(1,1,1,"tester")


def insert_chapter_table(summary):
    connexion = sqlite3.connect("bdd.db")
    curseur = connexion.cursor()
    curseur.execute("INSERT INTO Chapter VALUES( ? , ? ) " , (None , summary))
    connexion.commit()
    connexion.close()

insert_chapter_table()
insert_chapter_table("text")
insert_chapter_table("summary")


def creer_caracter(prenom, nom, resume):
    connexion = sqlite3.connect("bdd.db")
    curseur = connexion.cursor()
    curseur.execute("INSERT INTO Caracter VALUES (?, ?, ?, ?);", (None, str(prenom), str(nom), str(resume)))
    connexion.commit()
    connexion.close()

creer_caracter()
creer_caracter("test2", "test3", "test4")


def insert_IsInChapter_table(ChapterId,CaracterId):
    connexion = sqlite3.connect("bdd.db")
    curseur = connexion.cursor()
    curseur.execute("INSERT INTO IsInChapter VALUES( ? , ? ) " , (ChapterId , CaracterId))
    connexion.commit()
    connexion.close()

insert_IsInChapter_table(1,1)



# Lecture des fonctions (read)

def read_user(username,password):
    connexion = sqlite3.connect("bdd.db")
    curseur = connexion.cursor()
    curseur.execute("SELECT UserID, Username, Password FROM User WHERE Username = ? and Password = ?",(username,password));
    return curseur.fetchall()

def read_paragraph(ChapterID, UserID,description):
    connexion = sqlite3.connect("bdd.db")
    curseur = connexion.cursor()
    curseur.execute("""SELECT ParagraphID, ChapterID, UserID, date, text 
                        FROM Paragraph 
                        JOIN User ON ParagraphID = UserID
                        JOIN Chapter ON ParagraphID = ChapterID
                        WHERE date = ? and text = ?""",(None, ChapterID, UserID, str(datetime.now()), str(description)));
    return curseur.fetchall()





# Update des fonctions

def maj_nom_utilisateur(id,nom):
    connexion = sqlite3.connect("bdd.db")
    curseur = connexion.cursor()
    curseur.execute("UPDATE User SET Name = ? WHERE UserID = ? ;",(nom,id))
    connexion.commit()
    connexion.close()

def maj_password_utilisateur(id,password):
    connexion = sqlite3.connect("bdd.db")
    curseur = connexion.cursor()
    curseur.execute("UPDATE User SET Password = ? WHERE UserID = ? ;",(password,id))
    connexion.commit()
    connexion.close()


def maj_commentaire(id,text_commentaire):
    connexion = sqlite3.connect("bdd.db")
    curseur = connexion.cursor()
    curseur.execute("UPDATE Comment SET text = ? WHERE CommentID = ? ;",(text_commentaire,id))
    connexion.commit()
    connexion.close()

maj_commentaire(3,"test_modifier")



# Delete des fonctions

def supprime_utilisateur(id):
    connexion = sqlite3.connect('bdd.db')
    curseur = connexion.cursor()
    curseur.execute("DELETE FROM User WHERE userID = ? ;",(id,))
    connexion.commit()

def supprime_commentaire(id):
    connexion = sqlite3.connect('bdd.db')
    curseur = connexion.cursor()
    curseur.execute("DELETE FROM Comment WHERE CommentID = ? ;",(id,))
    connexion.commit()

supprime_commentaire(2)























