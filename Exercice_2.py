def isprime(num):
    for n in range(2,int(num**0.5)+1):
        if num%n==0:
            return False
    return True

type = int(input("Que voulez-vous faire ?\nCrypter un message => 1\nDécrypter un message => 2\n=> "))

if type == 1:

    m = input("Veuillez saisir une lettre minuscule qui va servir de message : ")
    print(f"Le code ASCII de la lettre est : {ord(m)}")
    m = ord(m)

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

    C = m**e % r

    print(f"Calcul du message crypté C ({m}^{e} modulo {r}): {C}")

if type == 2:
    MessageCrypte = int(input("Veuillez saisir le message crypté : "))
    d = int(input("Veuillez saisir la clé privée : "))
    r = int(input("Veuillez saisir la clé publique : "))
    Message = MessageCrypte**d % r
    print(f"Message décrypté ({MessageCrypte}^{d} modulo {r}) : {Message}")