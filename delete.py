import crud

def effacer_chapitre():
    for i in range(3,14):
        crud.supprime_chapitre_sommaire(i)
def ecrire_paragraphe():
    crud.insert_chapter_table("Ceci est est le chapitre 2")

def supprimer_paragraphe():
    for i in range(1,32):
        crud.supprime_paragraphe(i)
def inserer_paragraph():
    crud.creer_paragraph(2,3,"C'est le paragraphe du chapitre 2")
inserer_paragraph()
def effacer_character():
    for i in range(14):
        crud.supprime_caractere(i)
def ajouter_caracter():
    crud.creer_caracter("Omar","Maoka","Personnage n°2")



def efface_Is_in_chapter():
    crud.supprime_Is_In_Chapter(1)

def ajoute_Is_in_Chapter():
    crud.insert_IsInChapter_table(21,1)
ajoute_Is_in_Chapter()
def ajoute_Is_in_Chapter():
    liste_info_caractere =crud.read_chapter_charactere()
    print(liste_info_caractere)
def ajoute_commentaire():
    crud.ajout_commentaire(1,1,"Tester")
