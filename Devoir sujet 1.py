# Script pour générer un dictionnaire de mots basé sur trois paramètres d'entrée

def generate_dictionary(name, birthdate, location):
    """
    Génère un dictionnaire de mots potentiels à partir de trois paramètres.
    
    Args:
        name (str): Nom de la personne
        birthdate (str): Date de naissance (format JJMMAAAA, ex: 01011990)
        location (str): Lieu (ville ou autre information)
    
    Returns:
        list: Liste de mots potentiels pour un dictionnaire
    """
    # Initialisation de la liste du dictionnaire
    dictionary = []
    
    # Nettoyage des entrées
    name = name.lower().strip()
    location = location.lower().strip()
    birthdate = birthdate.strip()
    
    # Ajout des paramètres de base
    dictionary.extend([name, location, birthdate])
    
    # Variations du nom
    dictionary.append(name.replace(" ", ""))  # Sans espaces
    dictionary.append(name.split()[0] if " " in name else name)  # Prénom uniquement
    dictionary.append(name.split()[-1] if " " in name else name)  # Nom de famille uniquement
    dictionary.append(name + birthdate[-4:])  # Nom + année
    dictionary.append(name + birthdate[:2])   # Nom + jour
    dictionary.append(name + birthdate[2:4])  # Nom + mois
    
    # Variations de la date de naissance
    dictionary.append(birthdate[-4:])  # Année
    dictionary.append(birthdate[:2])   # Jour
    dictionary.append(birthdate[2:4])  # Mois
    dictionary.append(birthdate[:4] + birthdate[-4:])  # JJMM + AAAA
    
    # Variations du lieu
    dictionary.append(location.replace(" ", ""))  # Sans espaces
    dictionary.append(name + location)  # Nom + lieu
    dictionary.append(location + birthdate[-4:])  # Lieu + année
    
    # Ajout de quelques variations communes
    common_suffixes = ["123", "2023", "!", "@", "password"]
    for word in [name, location, birthdate[-4:]]:
        for suffix in common_suffixes:
            dictionary.append(word + suffix)
    
    # Suppression des doublons et retour
    return list(set(dictionary))

# Exemple d'utilisation
if __name__ == "__main__":
    # Paramètres d'exemple
    name = "Jean Dupont"
    birthdate = "01011990"
    location = "Paris"
    
    # Génération du dictionnaire
    wordlist = generate_dictionary(name, birthdate, location)
    
    # Affichage du dictionnaire
    print("Dictionnaire généré :")
    for word in wordlist:
        print(word)