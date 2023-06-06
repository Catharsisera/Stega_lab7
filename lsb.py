from PIL import Image
from bit_func import *
from random import choice

def lsbr(cont, mesbit, start = 0, step = 1):
    e = start
    for i in mesbit:
        cont[e] ^= cont[e] % 2      #Обнуляем последний бит
        cont[e] ^= i                #Заменяем бит на бит сообщения
        e += step
    return cont

def lsbm(cont, mesbit, start = 0, step = 1):
    e = start
    for i in mesbit:
        if cont[e] % 2 != i:    #Если бит внедряемого сообщения не равен LSB
            cont[e] += choice([-1, 1])
        e += step
    return cont

def lsbr3(cont, mesbit, start = 0, step = 1):
    e = start
    for i in mesbit:
        if e % 3 == 0:
            cont[e//3] -= cont[e//3] % 8       #Обнуляем три последних бита
        cont[e//3] ^= i * 2 ** (e % 3)         #Заменяем бит контейнера на бит сообщения
        e += step
    return cont

def lsbm3(cont, mesbit, start=0, step=1):
    e = start
    for i in mesbit:
        if cont[e//3] // 2 ** (e % 3) % 2 != i:
            cont[e//3] += choice([-1, 1]) * 2 ** (e % 3)
        e += step
    return cont

image_path = Image.open('part.bmp')
message = "".join(open("input.txt").readlines())
print(message)
message += "u98^%r*#8"         #метка окончания сообщения
encoded_message = message.encode('cp1251')    #кодируется в байты
encoded_mess_bits = []
for i in encoded_message:
    encoded_mess_bits.extend(to_bits(i))
# print(bits)

pix = image_path.load()     #загрузка пикселей изображения
pixels = []

for x in range(image_path.size[0]):
    for y in range(image_path.size[1]):
        pixels.extend(pix[x, y])    #значения каждого пикселя добавляются в список

"""LSBR R1"""
newpixels = lsbr(pixels, encoded_mess_bits)
newpix = [(newpixels[i], newpixels[i + 1], newpixels[i + 2]) for i in
          range(0, len(newpixels), 3)]  #преобразуется в список кортежей RGB для создания нового изображения

img = Image.new(image_path.mode, image_path.size)   #cоздается новое изображение
pixelsNew = img.load()

for i in range(img.size[0]):    #новым пикселям newpix присваиваются значения пикселей из newpixels
    for j in range(img.size[1]):
        pixelsNew[i, j] = newpix[j + img.size[1] * i]
#img.show()
img.save("LSBR_TEST_R1.bmp")

"""LSBM R1"""
newpixels = lsbm(pixels, encoded_mess_bits)
newpix = [(newpixels[i], newpixels[i + 1], newpixels[i + 2]) for i in
          range(0, len(newpixels), 3)]

img = Image.new(image_path.mode, image_path.size)
pixelsNew = img.load()
for i in range(img.size[0]):
    for j in range(img.size[1]):
        pixelsNew[i, j] = newpix[j + img.size[1] * i]
#img.show()
img.save("LSBM_TEST_R1.bmp")

"""LSBR R0.25"""
newpixels = lsbr(pixels, encoded_mess_bits, 0, 4)
newpix = [(newpixels[i], newpixels[i + 1], newpixels[i+2]) for i in
          range(0, len(newpixels), 3)]

img = Image.new(image_path.mode, image_path.size)
pixelsNew = img.load()

for i in range(img.size[0]):
    for j in range(img.size[1]):
        pixelsNew[i, j] = newpix[j + img.size[1] * i]
#img.show()
img.save("LSBR_TEST_R0.25.bmp")

"""LSBM R0.25"""
newpixels = lsbm(pixels, encoded_mess_bits, 0, 4)
newpix = [(newpixels[i], newpixels[i + 1], newpixels[i + 2]) for i in
          range(0, len(newpixels), 3)]

img = Image.new(image_path.mode, image_path.size)
pixelsNew = img.load()

for i in range(img.size[0]):
    for j in range(img.size[1]):
        pixelsNew[i,j] = newpix[j + img.size[1] * i]
#img.show()
img.save("LSBM_TEST_R0.25.bmp")

"""LSBR R3"""
newpixels = lsbr3(pixels, encoded_mess_bits)
newpix = [(newpixels[i], newpixels[i + 1], newpixels[i + 2]) for i in
          range(0, len(newpixels), 3)]

img = Image.new(image_path.mode, image_path.size)
pixelsNew = img.load()
for i in range(img.size[0]):
    for j in range(img.size[1]):
        pixelsNew[i, j] = newpix[j + img.size[1] * i]
#img.show()
img.save("LSBR_TEST_R3.bmp")

"""LSBM R3"""
newpixels = lsbm3(pixels, encoded_mess_bits)
newpix = [(newpixels[i],newpixels[i+1],newpixels[i+2]) for i in range(0,len(newpixels),3)]

img = Image.new(image_path.mode, image_path.size)
pixelsNew = img.load()

for i in range(img.size[0]):
    for j in range(img.size[1]):
        pixelsNew[i,j] = newpix[j + img.size[1] * i]
#img.show()
img.save("LSBM_TEST_R3.bmp")

image_path.close()
img.close()