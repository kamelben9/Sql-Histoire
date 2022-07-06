
import sqlite3
from datetime import datetime

#Creation des fonctions (create)

def ajout_utilisateur(user_name,password):
    connexion = sqlite3.connect('bdd.db')
    curseur = connexion.cursor()
    curseur.execute("INSERT INTO User  Values (?,?,?);",(None,str(user_name),str(password)))
    connexion.commit()
    connexion.close()
#ajout_utilisateur()  

def insert_challenge_table(UserId, ParagraphId, text, vote):

    vote = 0
    
    connexion = sqlite3.connect("bdd.db")
    curseur = connexion.cursor()
    curseur.execute("INSERT INTO Challenge VALUES( ? , ? , ?, ?) " , (UserId , ParagraphId, str(text), int(vote)))
    connexion.commit()
    connexion.close()

#insert_challenge_table()

def creer_paragraph(ChapterID, UserID, description):
    connexion = sqlite3.connect("bdd.db")
    curseur = connexion.cursor()
    curseur.execute("INSERT INTO Paragraph VALUES (?, ?, ?, ?, ?);", (None, ChapterID, UserID, str(datetime.now()), str(description)))
    connexion.commit()
    connexion.close()

#creer_paragraph(1,1,"toto")


def ajout_commentaire(user_id,chapter_id,date,text):
    connexion = sqlite3.connect('bdd.db')
    curseur = connexion.cursor()
    curseur.execute("INSERT INTO Comment  Values (?,?,?,?,?);",(None,user_id,chapter_id,date,text))
    connexion.commit()
    connexion.close()
#ajout_commentaire(1,1,1,"tester")


def insert_chapter_table(summary):
    connexion = sqlite3.connect("bdd.db")
    curseur = connexion.cursor()
    curseur.execute("INSERT INTO Chapter VALUES( ? , ? ) " , (None , summary))
    connexion.commit()
    connexion.close()

#insert_chapter_table("text")
#insert_chapter_table("summary")


def creer_caracter(prenom, nom, resume):
    connexion = sqlite3.connect("bdd.db")
    curseur = connexion.cursor()
    curseur.execute("INSERT INTO Caracter VALUES (?, ?, ?, ?);", (None, str(prenom), str(nom), str(resume)))
    connexion.commit()
    connexion.close()

#creer_caracter("test2", "test3", "test4")


def insert_IsInChapter_table(ChapterId,CaracterId):
    connexion = sqlite3.connect("bdd.db")
    curseur = connexion.cursor()
    curseur.execute("INSERT INTO IsInChapter VALUES( ? , ? ) " , (ChapterId , CaracterId))
    connexion.commit()
    connexion.close()

#insert_IsInChapter_table(1,1)



# Lecture des fonctions (read)
def lire_données_commentaire_via_identifiant(user_id):
    connexion = sqlite3.connect("bdd.db")
    curseur = connexion.cursor()
    curseur.execute("Select CommentID,UserID,ChapterID,date,text from Comment WHERE UserID = ? ;",(str(user_id)),)
    return curseur.fetchall()


def lire_données_chapitre(chapter_id):
    connexion = sqlite3.connect("bdd.db")
    curseur = connexion.cursor()
    curseur.execute("Select Summary from Chapter WHERE ChapterID = ? ;",(str(chapter_id)),)
    return curseur.fetchall()


#print(lire_données_chapitre(2))
def read_user(username):
    connexion = sqlite3.connect("bdd.db")
    curseur = connexion.cursor()
    curseur.execute("SELECT * FROM User WHERE Username = ? ;",(username,))
    return curseur.fetchall()


def read_paragraph(paragraphe_id):
    connexion = sqlite3.connect("bdd.db")
    curseur = connexion.cursor()
    curseur.execute("""SELECT Date, Text,Username 
    FROM Paragraph 
    JOIN User On Paragraphe.UserID = User.UserID 
    WHERE ParagraphID = ? ;""",(str(datetime.now(),), str(paragraphe_id)))
    return curseur.fetchall()

def lire_dernier_paragraph():
    connexion = sqlite3.connect("bdd.db")
    curseur = connexion.cursor()
    curseur.execute("""SELECT Username,ChapterID,Paragraph.UserID,date,text
    FROM Paragraph
    Join User ON   Paragraph.UserID=User.UserID ORDER BY date DESC ;""")
    return curseur.fetchall()

def read_caracter(CaracterID):
    connexion = sqlite3.connect("bdd.db")
    curseur = connexion.cursor()
    curseur.execute("SELECT FistName, LastName, Resume FROM Caracter WHERE CaracterID = ? ;", (str(CaracterID)),)
    return curseur.fetchall()

def read_chapter(ChapterID):
    connexion = sqlite3.connect("bdd.db")
    curseur = connexion.cursor()
    curseur.execute("""SELECT Chapter.ChapterID,Summary,Paragraph.Text FROM Chapter 
    JOIN Paragraph ON Chapter.ChapterID=Paragraph.ChapterID 
    WHERE Chapter.ChapterID = ? ;""" ,(str(ChapterID),))
    return curseur.fetchall()


#read_caracter()




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


def maj_commentaire(comment_id,text_commentaire):
    connexion = sqlite3.connect("bdd.db")
    curseur = connexion.cursor()
    curseur.execute("UPDATE Comment SET text = ? WHERE CommentID = ? ;",(text_commentaire,comment_id))
    connexion.commit()
    connexion.close()

#maj_commentaire(3,"test_modifier")

def maj_chapitre_sommaire(chapter_id,sommaire):
    connexion = sqlite3.connect("bdd.db")
    curseur = connexion.cursor()
    curseur.execute("UPDATE Chapter SET Summary = ? WHERE ChapterID = ? ;",(chapter_id,sommaire))
    connexion.commit()
    connexion.close()   


def update_caracter_resume(CaracterID,resume):
    connexion = sqlite3.connect("bdd.db")
    curseur = connexion.cursor()
    curseur.execute("UPDATE Caracter SET Resume = ? WHERE Resume = ? ;",(CaracterID, resume))
    connexion.commit()
    connexion.close()

# Delete des fonctions

def supprime_utilisateur(id):
    connexion = sqlite3.connect('bdd.db')
    curseur = connexion.cursor()
    curseur.execute("DELETE FROM User WHERE userID = ? ;",(id,))
    connexion.commit()
    connexion.close()

def supprime_commentaire(id):
    connexion = sqlite3.connect('bdd.db')
    curseur = connexion.cursor()
    curseur.execute("DELETE FROM Comment WHERE CommentID = ? ;",(id,))
    connexion.commit()
    connexion.close()

#supprime_commentaire(2)

def supprime_chapitre_sommaire(chapter_id):
    connexion = sqlite3.connect('bdd.db')
    curseur = connexion.cursor()
    curseur.execute("DELETE FROM Chapter WHERE ChapterId = ? ;",(chapter_id,))
    connexion.commit()
    connexion.close()

def supprime_paragraphe(paragraphe_ID):
    connexion = sqlite3.connect('bdd.db')
    curseur = connexion.cursor()
    curseur.execute("DELETE FROM Paragraph WHERE ParagraphID = ? ;",(paragraphe_ID,))
    connexion.commit()
    connexion.close()
#supprime_chapitre_sommaire(1)






















