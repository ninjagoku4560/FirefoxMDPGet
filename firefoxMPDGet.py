import shutil,sys,time,random 
from pathlib import Path


#mets dans cette variable ton nom d'utilisateur (va dans C:\Users pour le trouver) 
NomDUtilisateur = "natha"

#veuillez mettre ici le nom du dossier de votre profile firefox
#il se compose d'un texte aleatoire.defaultrelease
NomDossier = "i4orzey3.default-release"

#######
#debug#
#######
Copy = False
#######
#debug#
#######


FilePath = "C:\\Users\\Public\\Documents"  
  
fKeyPath = "C:\\Users\\" + NomDUtilisateur + "\\AppData\\Roaming\\Mozilla\\Firefox\\Profiles\\" + NomDossier + "\\key4.db" 
fKeyName = "key4.db" 
fLoginPath = "C:\\Users\\" + NomDUtilisateur + "\\AppData\\Roaming\\Mozilla\\Firefox\\Profiles\\"+NomDossier+"\\logins.json" 


fLoginName = "logins.json" 
  
  
print("\033[0m Lancement du programme de recupération des mots de passes...")
print("\033[0m [+] recherche des fichiers") 
time.sleep(0.25) 
  
for i in range(random.randint(2, 7)): 
    sys.stdout.write(f"\033[0m\r [|] recherche du fichier {fKeyName}") 
    sys.stdout.flush() 
    time.sleep(0.1)
    sys.stdout.write(f"\r [/] recherche du fichier {fKeyName}") 
    sys.stdout.flush() 
    time.sleep(0.1) 
    sys.stdout.write(f"\r [-] recherche du fichier {fKeyName}") 
    sys.stdout.flush() 
    time.sleep(0.1)
    sys.stdout.write(f"\r [\] recherche du fichier {fKeyName}") 
    sys.stdout.flush() 
    time.sleep(0.1)
if Path(fKeyPath).exists(): 
   print("\033[1;32m\r [+] le fichier "+fKeyName+"  à été trouver") 
   F1 = True 
else:
    print("\033[1;31m\r [-] le fichier "+fKeyName+" n'as pas été trouver") 
    F1 = False 
time.sleep(1) 
  
for i in range(random.randint(2, 7)): 
    sys.stdout.write(f"\033[0m\r [|] recherche du fichier {fLoginName}") 
    sys.stdout.flush() 
    time.sleep(0.1)
    sys.stdout.write(f"\r [/] recherche du fichier {fLoginName}") 
    sys.stdout.flush() 
    time.sleep(0.1) 
    sys.stdout.write(f"\r [-] recherche du fichier {fLoginName}") 
    sys.stdout.flush() 
    time.sleep(0.1)
    sys.stdout.write(f"\r [\] recherche du fichier {fLoginName}") 
    sys.stdout.flush() 
    time.sleep(0.1)
if Path(fLoginPath).exists(): 
   print(f"\033[1;32m\r [+] le fichier {fLoginName} à été trouver") 
   F2 = True 
else:
    print(f"\033[1;31m\r [-] le fichier {fLoginName} n'as pas été trouver") 
    F2 = False 
time.sleep(1) 
  

if F1 == True and F2 == True: 
    print("\033[1;32m [+] tous les fichiers ont été trouver  ") 
    File = True 
else: 
    print("\033[1;31m [-] le fichier non trouver") 
    File = False 
    print("j'ai besoin des fichiers presents dans votre profile firefox") 
    print("%APPDATA%\Mozilla\Firefox\Profiles") 
  
time.sleep(1) 
  
  
#systeme de copie-colle 
if File == True and Copy == True: 
    try: 
        filePathKey = shutil.copy(fKeyPath,FilePath) 
        print(f"\033[1;32m [+] le fichier avec la clé déchiffrement à été copier")
        time.sleep(1) 
    except: 
        print(f"\033[1;31m [-] le fichier avec la clé de déchiffrement n'a pas été copier") 
        print("    Merci de vérifier si le chemin entrer est le bon") 
    time.sleep(1)
    try: 
        filePathLogin = shutil.copy(fLoginPath,FilePath) 
        print(f"\033[1;32m [+] le fichier avec les mots de passe crypter à été copier") 
        time.sleep(1) 
    except: 
        print(f"\033[1;31m [-] le fichier avec les mots de passe crypter n'a pas été copier") 
        print("    Merci de vérifier si le chemin entrer est le bon")

print("\033[0m Chargement de firefox_decrypt...")
try:
    import firefox_decrypt
    FD = True
except:
    print("firefox_decrypt.py not found")
    FD = False

if FD == True:
    firefox_decrypt.run_ffdecrypt()


i = input("\033[0m")
