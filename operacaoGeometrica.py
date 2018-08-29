import numpy as np
from PIL import Image
import math


def reflexao (mat , m , n ,eixo):
    x = lambda x : x
    y = lambda y : y
    saida = np.zeros([m,n])
    if eixo == 1 :
        x = lambda x: m -1 -x
    else:
        y = lambda y: n-1 -y 
    for i in range(m):
        for j in range(n):
            saida[i,j] = mat[x(i),y(j)]
    img  = Image.fromarray(saida)
    Image._show(img)


''' def rotacao(mat, m , n , angulo):
   # usando centro da imagem utilizado como centro de rotação
    x0  = 0.5 * (m)
    y0  = 0.5 * (n)
    #calcula o novo x e y do pixel da imagem 
    x  = lambda x, y:int( x*math.cos(math.radians(angulo)) - y*math.sin(math.radians(angulo)))
    y  = lambda x,y: int (x*math.cos(angulo) + y*math.sin(angulo))
    saida = np.zeros([m,n])
   # a  = abs(int(x(m-1,n-1) + x0))
    #b  = abs(int(y(m-1,n-1) + y0))
    saida = np.zeros([m,n])
    #print('m:{} n: {}'.format(a,b))
    for i in range(m):
        for j in range(n):
            xb = int(x(i-x0,j-y0) + x0)
            yb = int(y(i-x0,j-y0) + y0)
            #print(xb,yb)
            if  xb < m and xb >=0 and yb >= 0 and yb < n:
                saida[i,j] = mat[xb,yb]
    img = Image.fromarray(saida)
    Image._show(img)
 



'''

if __name__ == '__main__':
    img  = Image.open('bolo1.jpg')
    #Image._show(img)
    img  = img.convert('L')
    matriz = np.asarray(img)
    while(True):
        print("1: reflexao no eixo x")
        print("2: reflexao no eixo y")
        eixo = input()
        m,n = matriz.shape
        print("m: {} n: {}".format(m , n))
        #rotacao(matriz,m,n,int(eixo))
        reflexao(matriz,m,n,int(eixo))
