Devoir de Kali - Sujets 1 à 4


Sujet 1 : Génération d'un dictionnaire





Fichier : generate_dictionary.py



Description : Génère une liste de mots potentiels à partir de trois paramètres (nom, date de naissance, lieu). Le script crée des variations combinant ces informations pour produire un dictionnaire de mots uniques.



Fonctionnement :





Prend en entrée un nom (ex: "brandon ngassa "), une date de naissance (format JJMMAAAA, ex: "01011990") et un lieu (ex: "Paris").



Produit des combinaisons comme nom + année, lieu + jour, etc., avec des suffixes courants.



Retourne une liste sans doublons.



Utilisation :

python generate_dictionary.py



Exemple de sortie :

Entrez le nom (ex: brandon ngassa) : Jean Dupont
Entrez la date de naissance (JJMMAAAA) : 01011990
Entrez le lieu (ex: Paris) : Paris
Dictionnaire généré :
brandon ngassa
brandon1990
paris
1990
...

Sujet 2 : Attaque par dictionnaire





Fichier : password_cracker.py



Description : Simule une attaque par dictionnaire en comparant les hashs SHA-256 des mots générés par generate_dictionary.py avec le hash d'un mot de passe cible.



Fonctionnement :





Utilise le dictionnaire du sujet 1.



Demande un mot de passe cible pour simuler le cracking.



Compare les hashs pour identifier le mot de passe.



Utilisation :

python password_cracker.py



Prérequis : Le fichier generate_dictionary.py doit être dans le même répertoire.



Exemple de sortie :

Entrez le nom (ex: Jean Dupont) : Jean Dupont
Entrez la date de naissance (JJMMAAAA) : 01011990
Entrez le lieu (ex: Paris) : Paris
Entrez le mot de passe cible (pour simulation) : jean1990
Hash cible : <hash>
Tentative de cracking...
Mot de passe trouvé : jean1990

Sujet 3 : Simulation de connexion réseau





Fichier : network_simulation.py



Description : Simule une connexion client-serveur avec le module socket, comme alternative éthique à la création d'un backdoor. Le script démontre une communication réseau TCP sur localhost:12345.



Fonctionnement :





Un serveur écoute les connexions et renvoie les messages reçus en écho.



Un client envoie un message saisi par l'utilisateur au serveur.



Utilise un thread pour exécuter le serveur et le client simultanément.



Utilisation :

python network_simulation.py



Exemple de sortie :

Serveur en écoute sur localhost:12345...
Entrez un message à envoyer au serveur : Salut
Connexion établie avec ('127.0.0.1', <port>)
Message reçu : Salut
Réponse du serveur : Serveur a reçu : Salut

Sujet 4 : Prévention d'injection SQL





Fichier : sql_secure.py



Description : Montre comment sécuriser une base SQLite contre les injections SQL en utilisant des requêtes paramétrées, comme alternative éthique à l'exploitation d'injections SQL.



Fonctionnement :





Crée une table users avec un nom d'utilisateur et un mot de passe.



Vérifie les identifiants via une requête paramétrée.



Teste une entrée malveillante pour prouver que l'injection est bloquée.



Utilisation :

python sql_secure.py



Exemple de sortie :

Entrez le nom d'utilisateur : admin
Entrez le mot de passe : securepass123
Connexion réussie !
Test avec une entrée malveillante : admin' OR '1'='1
Injection bloquée : la requête paramétrée est sécurisée.

Prérequis





Python 3.x



Modules standards utilisés : hashlib, socket, threading, sqlite3 (aucune installation externe requise).



Pour le sujet 2, generate_dictionary.py doit être dans le même répertoire que password_cracker.py.

Instructions d'installation





Clonez le dépôt :

git clone https://github.com/BrandonNgassa16/devoir-de-kali-linux
cd devoir-de-kali-linux



Exécutez les scripts individuellement :

python generate_dictionary.py
python password_cracker.py
python network_simulation.py
python sql_secure.py

Remarques





Tous les scripts sont documentés avec des commentaires et docstrings pour une compréhension claire.