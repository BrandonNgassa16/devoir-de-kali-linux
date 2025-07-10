import hashlib

def crack_password(data_dict, password_to_crack):
    for key in data_dict.keys():
        hashed = hashlib.md5(data_dict[key].encode()).hexdigest()
        if hashed == password_to_crack:
            return f"Mot de passe trouvé : {data_dict[key]}"
    return "Mot de passe non trouvé."

# Exemple d'utilisation# Script pour simuler une attaque par dictionnaire sur un mot de passe

import hashlib
from generate_dictionary import generate_dictionary

def hash_password(password):
    """
    Génère un hash SHA-256 du mot de passe.
    
    Args:
        password (str): Mot de passe à hasher
    
    Returns:
        str: Hash SHA-256 du mot de passe
    """
    return hashlib.sha256(password.encode()).hexdigest()

def crack_password(target_hash, dictionary):
    """
    Tente de cracker un mot de passe en comparant les hashs avec ceux du dictionnaire.
    
    Args:
        target_hash (str): Hash du mot de passe cible
        dictionary (list): Liste de mots à tester
    
    Returns:
        str or None: Mot de passe trouvé ou None si non trouvé
    """
    for word in dictionary:
        if hash_password(word) == target_hash:
            return word
    return None

# Exemple d'utilisation
if __name__ == "__main__":
    # Paramètres pour générer le dictionnaire
    name = "Jean Dupont"
    birthdate = "01011990"
    location = "Paris"
    
    # Génération du dictionnaire
    wordlist = generate_dictionary(name, birthdate, location)
    
    # Simulation d'un mot de passe cible (par exemple, "jean1990")
    target_password = "jean1990"
    target_hash = hash_password(target_password)
    
    print(f"Hash cible : {target_hash}")
    print("Tentative de cracking...")
    
    # Tentative de cracking
    result = crack_password(target_hash, wordlist)
    
    if result:
        print(f"Mot de passe trouvé : {result}")
    else:
        print("Mot de passe non trouvé dans le dictionnaire.")
if __name__ == "__main__":
    data_dict = {'user1': 'password123', 'user2': '123456', 'user3': 'letmein'}
    password_to_crack = input("Entrez le mot de passe hashé à cracker : ")
    
    result = crack_password(data_dict, password_to_crack)
    print(result)