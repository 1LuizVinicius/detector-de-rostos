# Usar pip install cv2
import cv2

# Carregar modelo
face_cascade = cv2.CascadeClassifier('exemplo1.png')

# Carrega imagem
img = cv2.imread('exemplo2.png')

# Converter para escala em cinza
gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

# Detectar rostos
faces = face_cascade.detectMultiScale(gray, 1.1, 4)

# Desenhar retangunlo no rosto detectado
for (x, y, w, h) in faces:
    cv2.rectangle(img, (x, y), (x+w, y+h), (255, 0, 0), 2)

# Mostrar resultado
cv2.imshow('img', img)
cv2.waitkey()