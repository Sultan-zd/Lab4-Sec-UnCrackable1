# UnCrackable Level 1 - Reverse Engineering Lab

Une analyse de sécurité complète (Audit SAST) de l'application vulnérable Android "UnCrackable Level 1", développée pour mettre en pratique la décompilation, le contournement des protections anti-débogage et la cryptographie appliquée.

### Fonctionnalités de l'Audit

* **Rétro-Ingénierie Java :** Décompilation de l'APK et analyse du flux d'exécution métier via le bytecode Dalvik.
* **Analyse du Manifeste :** Extraction des informations critiques et cartographie de la surface d'attaque.
* **Contournement des Protections (Bypass) :** Identification des mécanismes de détection d'environnement Root et de débogueurs intégrés à l'application.
* **Casse Cryptographique :** Analyse de l'implémentation de la fonction de hachage et du chiffrement (AES/ECB/PKCS5Padding).
* **Scripting Offensif :** Création d'un script d'automatisation en Python permettant d'extraire et de déchiffrer le mot de passe final à la volée.

### Technologies & Outils

* **Outil d'Analyse :** JADX-GUI (Décompilateur statique)
* **Langages :** Java (Lecture du code cible), Python (Script de déchiffrement)
* **Bibliothèques Externes :** `pycryptodome` (pour l'attaque cryptographique AES)
* **Environnement :** Windows

### Démonstration & Rapport

Le compte-rendu détaillé de la méthodologie (vulnérabilités trouvées, explications du code et étapes de contournement) est disponible directement dans le fichier `rapport.txt`.

### Installation & Reproductibilité

Clonez le dépôt pour auditer l'application vous-même :
```cmd
git clone https://github.com/Sultan-zd/Lab1-Sec-UnCrackable1.git
```
Pour exécuter le script de déchiffrement depuis l'invite de commandes Windows (CMD ou PowerShell) :
1. Installez la bibliothèque cryptographique requise (si nécessaire) :
   ```cmd
   pip install pycryptodome
3. Lancez le script d'extraction :
   ```cmd
   python decrypt_secret.py
