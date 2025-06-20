def generate_data_dict(param1, param2, param3):
    data_dict = {
        'param1': param1,
        'param2': param2,
        'param3': param3
    }
    return data_dict

# Exemple d'utilisation
if __name__ == "__main__":
    param1 = input("Entrez le premier paramètre : ")
    param2 = input("Entrez le deuxième paramètre : ")
    param3 = input("Entrez le troisième paramètre : ")
    
    result = generate_data_dict(param1, param2, param3)
    print(result)