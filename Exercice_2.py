import re
import numpy as np

def isprime(num):
    for n in range(2,int(num**0.5)+1):
        if num%n==0:
            return False
    return True

type = int(input("Que voulez-vous faire ?\nCrypter un message => 1\nDécrypter un message => 2\n=> "))

if type == 1:

    lettres = []

    m = input("Veuillez saisir une phrase qui va servir de message : ")
    for lettre in m:
        lettres.append(ord(lettre))

    p = int(input("Veuillez définir P (nombre premier) : "))
    while isprime(p) == False:
        print(f"Le chiffre {p} n'est pas un nombre premier")
        p = int(input("Veuillez définir P (nombre premier) : "))

    q = int(input("Veuillez définir Q (nombre premier) : "))
    while isprime(q) == False:
        print(f"Le chiffre {q} n'est pas un nombre premier")
        q = int(input("Veuillez définir Q (nombre premier) : "))

    while p == q:
        print("P et Q ne peuvent pas être identiques")
        q = int(input("Veuillez définir Q (nombre premier) : "))

    e = int(input(f"Veuillez définir E (nombre premier) : "))
    while isprime(e) == False:
        print(f"Le chiffre {e} n'est pas un nombre premier")
        e = int(input(f"Veuillez définir E (nombre premier) : "))

    r = p * q
    z = (p - 1) * (q - 1)

    d = 0.1 # Clé de décryptage
    n = 0
    while d.is_integer() == False:
        d = ((z * n) + 1) / e
        print(f"Recherche du nombre entier (({z} * {n}) + 1) / {e}) = {((z * n) + 1) / e}")
        n+=1

    print(f"Calcul de la clé d'encryptage (({z} * {n - 1}) + 1) / {e}) = {d}")

    print(f"Clé publique (P * Q) => ({p} * {q}) : {r}")
    print(f"Clé privée : {d}")

    Blocs = []
    bloc = 1
    for m in lettres:
        C = m**e % r
        print(f"Calcul du bloc {bloc} ({m}^{e} modulo {r}): {C}")
        Blocs.append(C)
        bloc+=1

    s = ','.join(str(x) for x in Blocs)
    print(f"Affichage simplifié des blocs : {s}")

if type == 2:

    BlocsCryptes = input("Veuillez saisir les blocs séparés par une virgule (ex: 50,85,45) : ")
    d = int(input("Veuillez saisir la clé privée : "))
    r = int(input("Veuillez saisir la clé publique : "))

    B = re.split(',', BlocsCryptes)
    Blocs = np.asarray(B, dtype=np.int64, order='C')
    print(Blocs)

    LettresDecryptees = []
    for message in Blocs:
        MessageDecrypte = message**d % r
        print(f"{message} ** {d} % {r} = {MessageDecrypte}")
        LettresDecryptees.append(chr(MessageDecrypte))
    D = "".join(LettresDecryptees)
    print(f"Message décrypté : {D}")

