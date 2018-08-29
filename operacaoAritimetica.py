import numpy as np
from PIL import Image

def soma(mat1,mat2,m,n):
	saida = np.zeros([m,n])
	print(saida.shape)
	for i in range(m):
		for j in range(n):
			#saida[i,j] = (mat1[i,j]+ mat2[i,j])//2
			if mat1[i,j]+ mat2[i,j] > 255:
				saida[i,j] = 255
			else:
				saida[i,j] = mat1[i,j]+ mat2[i,j]
	img =  Image.fromarray(saida)
	Image._show(img)


def subitracao(mat1,mat2,m,n):
	saida = np.zeros([m,n])
	print(saida.shape)
	for i in range(m):
		for j in range(n):
			if mat1[i,j] - mat2[i,j] < 0:
				saida[i,j] = 0
			else:
				saida[i,j] = mat1[i,j] - mat2[i,j]
	img = Image.fromarray(saida)
	Image._show(img)




if __name__ == '__main__':
	img1 = Image.open('bolo1.jpg')
	img2 = Image.open('bolo2.jpg')
    #converte para escala de cinza
	img1 = img1.convert('L')
	img2 = img2.convert('L')
       #Image._show(img2)
    #converte objeto imagem para matriz
	matriz1  = np.asarray(img1)
	matriz2  = np.asarray(img2)
    #print(matriz2)
	m, n  = matriz1.shape
	print("numero de linhas {}".format(m))
	print("numero de colunas {}".format(n))
	soma(matriz1,matriz2,m,n)
	#subitracao(matriz1,matriz2,m,n)