import shutil,sys,time,random
from pathlib import Path

#mets dans cette variable ton nom d'utilisateur (va dans C:\Users pour le trouver)
NomDUtilisateur = "user"
#mets ici l'endroit ou tu veux retrouver les fichiers
#merci de remplacer les \ part deux \\ car sinon cela ne fonctionne pas
FilePath = "C:\\Users\\Public\\Documents"



fKeyPath = "C:\\Users\\" + NomDUtilisateur + "\\AppData\\Roaming\\Mozilla\\Firefox\\Profiles\\i4orzey3.default-release\\key4.db"
fKeyName = "key4.db"
fLoginPath = "C:\\Users\\" + NomDUtilisateur + "\\AppData\\Roaming\\Mozilla\\Firefox\\Profiles\\i4orzey3.default-release\\logins.json"
fLoginName = "logins.json"



print("[+] recherche des fichiers")
time.sleep(0.25)


if Path(fKeyPath).exists():
    #boucle pour raffraichir au cas où
    for i in range(random.randint(1, 4)):
        sys.stdout.write(f"\r[|] recherche du fichier {fKeyName}")
        sys.stdout.flush()
        time.sleep(0.1)
        sys.stdout.write(f"\r[/] recherche du fichier {fKeyName}")
        sys.stdout.flush()
        time.sleep(0.1)
        sys.stdout.write(f"\r[-] recherche du fichier {fKeyName}")
        sys.stdout.flush()
        time.sleep(0.1)
        sys.stdout.write(f"\r[\] recherche du fichier {fKeyName}")
        sys.stdout.flush()
        time.sleep(0.1)

    print("\r[+] fichier "+fKeyName+" trouver")
    F1 = True
else:
    print("\r[-] fichier "+fKeyName+" non trouver")
    F1 = False
    
  
if Path(fLoginPath).exists():
     #boucle pour raffraichir au cas où
    for i in range(random.randint(1, 4)):
        sys.stdout.write(f"\r[|] recherche du fichier {fLoginName}")
        sys.stdout.flush()
        time.sleep(0.1)
        sys.stdout.write(f"\r[/] recherche du fichier {fLoginName}")
        sys.stdout.flush()
        time.sleep(0.1)
        sys.stdout.write(f"\r[-] recherche du fichier {fLoginName}")
        sys.stdout.flush()
        time.sleep(0.1)
        sys.stdout.write(f"\r[\] recherche du fichier {fLoginName}")
        sys.stdout.flush()
        time.sleep(0.1)

    print("\r[+] fichier "+fLoginName+" trouver")
    F2 = True
else:
    print("\r[-] fichier "+fLoginName+" non trouver")
    F2 = False
    
    
if F1 == True and F2 == True:
    print("[+] tous les fichiers ont été trouver")
    File = True
else:
    print("[-] fichier non trouver")
    File = False
    print("j'ai besoin des fichiers presents dans votre profile firefox")
    print("%APPDATA%\Mozilla\Firefox\Profiles")
    
time.sleep(1)


#systeme de copie-colle
if File == True:
    try:
        filePathKey = shutil.copy(fKeyPath,FilePath)
        print("[+] le fichier avec la clé déchiffrement à été copier")
        time.sleep(1)
    except:
        print("[-] le fichier avec la clé de déchiffrement n'a pas été copier")
        print("    Merci de vérifier si le chemin entrer est le bon")
    try:
        filePathLogin = shutil.copy(fLoginPath,FilePath)
        print("[+] le fichier avec les mots de passe crypter à été copier")
        time.sleep(1)
    except:
        print("[-] le fichier avec les mots de passe crypter n'a pas été copier")
        print("    Merci de vérifier si le chemin entrer est le bon")