#importando biblioteca
import os
import cv2

#criando caminho
caminho = "image"

image = []

#repetição de um comando 
for file in os.listdir(caminho):
    name, ext = os.path.splitext(file)
#verificando a extenção da image(gif, png, jpg, jpeg, jfif)
    if ext in ['.gif', '.png', '.jpg', '.jpeg','.jfif']:
        file_name = caminho+"/"+file

        print(file_name)
#append add um novo item a matriz = lista               
        image.append(file_name)
#len representa a quantidade de items que tem na matriz = lista        
print(len(image))
count = len(image)

frame = cv2.imread(image[0])
height, width, channels = frame.shape
size = (width, height)
print(size)

out = cv2.VideoWriter('project.mp4', cv2.VideoWriter_fourcc('DIVX'), 5, size)

for i in range(cont-1, 0, 1):
    frame = cv2.imread(image[i])
    out.write(frame)
    
out.release()
print('concluido')