import cv2
import numpy as np
from matplotlib import pyplot as plt
import math


# Exercício 1


# Exercício 1


def aplica_filtro(img, l, c, mask, colunas):
    a = colunas // 2

    sum = 0
    for x in range(colunas):
        posL = l - (a - x)
        for y in range(colunas):
            posC = c - (a - y)
            sum = img[posL][posC] * mask[x][y]

    return sum


if __name__ == "__main__":

    img = cv2.imread("/FotoQuestao1.jpg")

    print("Imagem Original")
    cv2_imshow(img)

    kernel5x5 = np.ones((5, 5), np.float32) / 25
    kernel7x7 = np.ones((7, 7), np.float32) / 49
    kernel9x9 = np.ones((9, 9), np.float32) / 81

    altura, largura, canais = img.shape

    listaImagens = [img.copy(), img.copy(), img.copy()]

    # aplicando filtro média 5x5
    var_aux = 5 // 2
    for l in range(1, altura - var_aux):
        for c in range(1, largura - var_aux):
            listaImagens[0][l][c] = aplica_filtro(img, l, c, kernel5x5, 5)

    print("Filtro 5x5")
    cv2.imshow(listaImagens[0])

    # aplicando filtro 7x7
    var_aux = 7 // 2
    for l in range(1, altura - var_aux):
        for c in range(1, largura - var_aux):
            listaImagens[1][l][c] = aplica_filtro(img, l, c, kernel7x7, 7)

    print("Filtro 7x7")
    cv2.imshow(listaImagens[1])

    # aplicando filtro 9x9
    var_aux = 9 // 2
    for l in range(1, altura - var_aux):
        for c in range(1, largura - var_aux):
            listaImagens[2][l][c] = aplica_filtro(img, l, c, kernel9x9, 9)

    print("Filtro 9x9")
    cv2.imshow(listaImagens[2])


