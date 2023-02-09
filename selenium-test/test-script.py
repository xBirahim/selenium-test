import string
from selenium import webdriver
from selenium.webdriver.common.by import By
from time import sleep
from random import choice

import cv2
import numpy as np
from pyzbar import pyzbar

# Fonctions :

def generate_random_text(length):
    characters = string.ascii_letters + string.digits + string.punctuation
    return ''.join(choice(characters) for _ in range(length))

def read_qr_code(image_path):
    # Charger l'image
    image = cv2.imread(image_path)
    
    # Trouver les codes QR dans l'image
    decoded = pyzbar.decode(image)
    
    # Boucle à travers tous les codes QR trouvés
    for obj in decoded:
        # Récupérer le message du code QR
        
        return obj.data.decode('utf-8')


# Créer une instance de navigateur
url = "http://localhost/codeqr/qrcodes/"
browser = webdriver.Edge()

# Naviguer vers la page web
browser.get(url)

# Vérifier le titre de la page

# Trouver le bouton
bouton = browser.find_elements(By.ID, "texte")[0]
# Cliquer sur le bouton
bouton.click()

# Trouver la textbox
textbox = browser.find_elements(By.NAME, "data")[0]
# Texte à encoder
text = generate_random_text(20)
textbox.send_keys(text)

# sleep(1)

btngenerate = browser.find_elements(By.ID, "btnGenerate")[0]
btngenerate.click()

# sleep(1)

qrcode = browser.find_elements(By.ID, "outputqr")[0]
imgqrcode = qrcode.screenshot("qr.png")
# # Vérifier les résultats
# print(f"str : {text}")
# print("qr : " + read_qr_code("qr.png"))

assert text == read_qr_code("qr.png")

# Fermer le navigateur
browser.quit()
