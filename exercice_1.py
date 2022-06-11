alphabet = ['T', 'A', 'D', 'U', 'J', 'V', 'X', 'C', 'G', 'W', 'M', 'Y', 'E', 'S', 'H', 'K', 'N', 'P', 'B', 'Q', 'R', 'L', 'Z', 'F', 'O', 'I', ' ']
lettres = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z', ' ']

print("Que souhaitez-vous faire ?\nChiffrer un message => 1\nDéchiffrer un message => 2")
type = int(input("Veuillez saisir le numéro de l'action à effectuer : "))

if type == 1:
    message = input("Veuillez saisir le message à chiffrer (uniquement des lettres majuscules et des espaces - max 80 caractères) : ")
    while len(message) == 0 or len(message) > 80:
        print("Le message doit respecter les règles suivantes : min 1 caractère et max 80 caractères")
        message = input("Veuillez saisir le message à chiffrer : ")
    chiffrage = str()
    for lettre in message:
        if lettre == ' ':
            chiffrage += alphabet[6]
        elif lettre == 'G':
            chiffrage += alphabet[26]
        else:
            chiffrage += alphabet[ord(lettre) - 65]
    print(f"Message chiffré : {chiffrage}")

if type == 2:
    message = input("Veuillez saisir le message à déchiffrer : ")
    decryptage = str()
    for lettre in message:
        if lettre == ' ':
            decryptage += lettres[6]
        elif lettre == 'X':
            decryptage += lettres[26]
        else:
            decryptage += lettres[alphabet.index(lettre)]
    print(f"Message déchiffré: {decryptage}")

