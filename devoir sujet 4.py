# sql_secure.py
# Script pour démontrer la prévention d'injection SQL avec des requêtes paramétrées

import sqlite3

def create_database():
    """
    Crée une base de données SQLite avec une table users.
    """
    conn = sqlite3.connect('example.db')
    cursor = conn.cursor()
    cursor.execute('''CREATE TABLE IF NOT EXISTS users (username TEXT, password TEXT)''')
    cursor.execute('''INSERT INTO users (username, password) VALUES (?, ?)''', ('admin', 'securepass123'))
    conn.commit()
    conn.close()

def secure_query(username, password):
    """
    Exécute une requête sécurisée avec des paramètres pour éviter l'injection SQL.
    
    Args:
        username (str): Nom d'utilisateur
        password (str): Mot de passe
    
    Returns:
        bool: True si les identifiants sont valides, False sinon
    """
    conn = sqlite3.connect('example.db')
    cursor = conn.cursor()
    
    # Requête paramétrée pour éviter l'injection SQL
    cursor.execute('''SELECT * FROM users WHERE username = ? AND password = ?''', (username, password))
    result = cursor.fetchone()
    
    conn.close()
    return result is not None

if __name__ == "__main__":
    # Créer la base de données
    create_database()
    
    # Test avec une entrée utilisateur
    username = input("Entrez le nom d'utilisateur : ")
    password = input("Entrez le mot de passe : ")
    
    # Vérification sécurisée
    if secure_query(username, password):
        print("Connexion réussie !")
    else:
        print("Identifiants incorrects.")
    
    # Test avec une tentative d'injection SQL
    malicious_input = "admin' OR '1'='1"
    print("\nTest avec une entrée malveillante :", malicious_input)
    if secure_query(malicious_input, "random"):
        print("Injection réussie (ce qui ne devrait pas arriver).")
    else:
        print("Injection bloquée : la requête paramétrée est sécurisée.")