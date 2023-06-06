from PIL import Image
from random import choice
from bit_func import *

def lsbr(cont, mesbit, start=0, step=1):
    e = start
    for i in mesbit:
        cont[e] ^= cont[e] % 2  # Обнуляем последний бит
        cont[e] ^= i  # Заменяем бит на бит сообщения
        e += step
    return cont

def lsbm(cont, mesbit, start=0, step=1):
    e = start
    for i in mesbit:
        if cont[e] % 2 != i:
            cont[e] += choice([-1, 1])
        e += step
    return cont

def lsbr3(cont, mesbit, start=0, step=1):
    e = start
    for i in mesbit:
        if e % 3 == 0:
            cont[e // 3] -= cont[e // 3] % 8  # Обнуляем три последних бита
        cont[e // 3] ^= i * 2 ** (e % 3)  # Заменяем бит на бит сообщения
        e += step
    return cont

def lsbm3(cont, mesbit, start=0, step=1):
    e = start
    for i in mesbit:
        if cont[e // 3] // 2 ** (e % 3) % 2 != i:
            cont[e // 3] += choice([-1, 1]) * 2 ** (e % 3)
        e += step
    return cont

def embed_text_into_image(image_path, text, embedding_function, **kwargs):
    message = text + "hs45*i!88"  # метка окончания сообщения
    encoded_message = message.encode('cp1251')  # кодируется в байты
    encoded_mess_bits = []
    for i in encoded_message:
        encoded_mess_bits.extend(to_bits(i))

    pix = image_path.load()  # загрузка пикселей изображения
    pixels = []
    for x in range(image_path.size[0]):
        for y in range(image_path.size[1]):
            pixels.extend(pix[x, y])  # значения каждого пикселя добавляются в список

    newpixels = embedding_function(pixels, encoded_mess_bits, **kwargs)
    newpix = [(newpixels[i], newpixels[i + 1], newpixels[i + 2]) for i in
              range(0, len(newpixels), 3)]  # преобразуется в список кортежей RGB для создания нового изображения

    embeddede_image = Image.new(image_path.mode, image_path.size)  # cоздается новое изображение
    embedded_new_pix = embeddede_image.load()
    for i in range(embeddede_image.size[0]):  # новым пикселям newpix присваиваются значения пикселей из newpixels
        for j in range(embeddede_image.size[1]):
            embedded_new_pix[i, j] = newpix[j + embeddede_image.size[1] * i]

    return embeddede_image

image_path = Image.open('24.bmp')
message = "".join(open("text.txt").readlines())
print(message)

embedded_image = embed_text_into_image(image_path, message, lsbm)
embedded_image.save("Embedded.bmp")

embedded_image = embed_text_into_image(image_path, message, lsbr)
embedded_image.save("Embedded_LSBR_R1.bmp")

embedded_image = embed_text_into_image(image_path, message, lsbr, step=4)
embedded_image.save("Embedded_LSBR_R0.25.bmp")

embedded_image = embed_text_into_image(image_path, message, lsbr3)
embedded_image.save("Embedded_LSBR_R3.bmp")

embedded_image = embed_text_into_image(image_path, message, lsbm)
embedded_image.save("Embedded_LSBM_R1.bmp")

embedded_image = embed_text_into_image(image_path, message, lsbm, step=4)
embedded_image.save("Embedded_LSBM_R0.25.bmp")

embedded_image = embed_text_into_image(image_path, message, lsbm3)
embedded_image.save("Embedded_LSBM_R3.bmp")

image_path.close()
embedded_image.close()
