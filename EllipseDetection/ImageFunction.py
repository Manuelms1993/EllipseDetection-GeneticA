from PIL import Image
import numpy as np
import matplotlib.pyplot as plt

def transformSquareImage(fileName):
    image = Image.open(fileName)
    imagenbw = image.convert("L")
    imagenbw.thumbnail((100, 100), Image.ANTIALIAS)
    imagenbw.save("sample.png")

def image2Matrix(fileName):
    m = np.asarray(Image.open(fileName).convert('L'))
    r = np.zeros((100,100))
    for i in range (m.shape[0]):
        for j in range (m.shape[1]):
            r[i][j]= 255 if m[i][j] > 50 else 0
    return r

def Matrix2Image(matrix):
    plt.imshow(matrix)
    plt.savefig('predict.png')