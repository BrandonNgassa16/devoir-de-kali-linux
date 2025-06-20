import hashlib

def crack_password(data_dict, password_to_crack):
    for key in data_dict.keys():
        hashed = hashlib.md5(data_dict[key].encode()).hexdigest()
        if hashed == password_to_crack:
            return f"Mot de passe trouvé : {data_dict[key]}"
    return "Mot de passe non trouvé."

# Exemple d'utilisation
if __name__ == "__main__":
    data_dict = {'user1': 'password123', 'user2': '123456', 'user3': 'letmein'}
    password_to_crack = input("Entrez le mot de passe hashé à cracker : ")
    
    result = crack_password(data_dict, password_to_crack)
    print(result)