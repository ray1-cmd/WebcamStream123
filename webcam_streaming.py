#Webcam stream by RAY1
import cv2
import requests
import numpy as np

url = "" #Replace with the webcam ip

# Effectue une requête GET à l'URL
response = requests.get(url, stream=True)

# Vérifie le code de réponse
if response.status_code == 200:
    # Acquisition des images en streaming et affichage de chaque image
    bytes_data = bytes()
    for chunk in response.iter_content(chunk_size=1024):
        bytes_data += chunk
        a = bytes_data.find(b'\xff\xd8')
        b = bytes_data.find(b'\xff\xd9')
        if a != -1 and b != -1:
            jpg = bytes_data[a:b+2]
            bytes_data = bytes_data[b+2:]
            img = cv2.imdecode(np.fromstring(jpg, dtype=np.uint8), cv2.IMREAD_COLOR)
            cv2.imshow('Webcam', img)
            if cv2.waitKey(1) == 27:
                break
else:
    print("La requête a échoué.")
