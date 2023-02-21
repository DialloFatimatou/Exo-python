from datetime import datetime

print("---------------Bonjour, Bienvenue sur ma page-------------------\n")

print("Appuie 1 pour vous Enregistrez\n")
print("Appuie 2 pour afficher la liste des personnes enregitrer\n")

a = int(input("Fait un choix entre 1-ENREGISTRER     2-LISTE \n"))
if a ==1:
    nom = input("Entrer votre nom: ")
    prenom = input("Entrer votre prenom: ")
    num = input("Entrer votre numero: ")
    mail = input("Entrer votre email: ") 
    date = datetime.now()
    jour = date.strftime('%Y-%m-%d')
    
    info = f"{jour}   {nom }   {prenom}   {num}   {mail} \t\n"
    with open("fichier.txt", "a+") as f:
        f.write(info)
        f.close()
elif a == 2 :
    with open("fichier.txt", "r") as f :
        print(f.read()) 
else:
    print("Erreur")
                   


