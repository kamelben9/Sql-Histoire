import hashlib



#ceci est le fichier pour les fonctions

def verif_user(username, password):


    utilisateur = {"username" : None, "password" : None}

    
    h = hashlib.new('sha256')
    h.update(password.encode())

    utilisateur["password"] = h.hexdigest()

    print(utilisateur["password"])
    

    if utilisateur["password"] :
        pass