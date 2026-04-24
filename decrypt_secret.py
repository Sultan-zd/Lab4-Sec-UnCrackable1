import base64
from Crypto.Cipher import AES

def decrypt_uncrackable_secret():
    print("[*] Début du déchiffrement du secret UnCrackable 1...")
    
    # 1. La clé extraite du code Java via JADX (en hexadécimal)
    key_hex = "8d127684cbc37c17616d806cf50473cc"
    key = bytes.fromhex(key_hex)
    
    # 2. Le secret chiffré extrait du code (en Base64)
    encrypted_secret_b64 = "5UJiFctbmgbDoLXmpL12mkno8HT4Lv8dlat8FxR2GOc="
    encrypted_bytes = base64.b64decode(encrypted_secret_b64)
    
    # 3. Déchiffrement avec AES en mode ECB
    cipher = AES.new(key, AES.MODE_ECB)
    decrypted_bytes = cipher.decrypt(encrypted_bytes)
    
    # Affichage du résultat en retirant les caractères de padding
    secret = decrypted_bytes.decode('utf-8').strip('\x0f\x0b\x0c\x0e\x00')
    print(f"[+] Succès ! Le secret est : {secret}")

if __name__ == "__main__":
    decrypt_uncrackable_secret()