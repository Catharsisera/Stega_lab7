from PIL import Image
from bit_func import *

def hamming(cont, mesbit):
    H = [
        [1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1],  #матрица проверки
        [0, 1, 1, 0, 0, 1, 1, 0, 0, 1, 1, 0, 0, 1, 1],
        [0, 0, 0, 1, 1, 1, 1, 0, 0, 0, 0, 1, 1, 1, 1],
        [0, 0, 0, 0, 0, 0, 0, 1, 1, 1, 1, 1, 1, 1, 1]
    ]

    for i in range(0, len(mesbit)//4):
        c_part = cont[i*15:(i+1)*15]        # выбирается блок из 15 пикселей для кодирования
        Hc = [sum([(H[r][e] * c_part[e]) % 2 for e in range(15)]) % 2 for r in range(4)]    #значения проверочных битов

        s = [
            (Hc[0] + mesbit[i * 4]) % 2,        #синдром на основе проверочных битов и битов из сообщения
            (Hc[1] + mesbit[i * 4 + 1]) % 2,
            (Hc[2] + mesbit[i * 4 + 2]) % 2,
            (Hc[3] + mesbit[i * 4 + 3]) % 2
        ]
        index = s[3] * 8 + s[2] * 4 + s[1] * 2 + s[0] - 1   #индекс ошибочного бита
        if index != -1:
            cont[i * 15 + index] ^= 1     #исправление ошибки путем инверсии бита в выбранном блоке пикселей с помощью операции XOR

    return cont

image_path = Image.open('24.bmp')
message = "".join(open("text.txt").readlines())
print(message)
message += "hs45*i!88"

encoded_message = message.encode('cp1251')
encoded_mess_bits = []
for i in encoded_message:
    encoded_mess_bits.extend(to_bits(i))

pix = image_path.load()
pixels = []
for x in range(image_path.size[0]):
    for y in range(image_path.size[1]):
        pixels.extend(pix[x, y])

newpixels = hamming(pixels, encoded_mess_bits)
newpix = [(newpixels[i], newpixels[i+1], newpixels[i+2]) for i in
          range(0, len(newpixels), 3)]
embeddede_image = Image.new(image_path.mode, image_path.size)
embedded_new_pix = embeddede_image.load()

for i in range(embeddede_image.size[0]):
    for j in range(embeddede_image.size[1]):
        embedded_new_pix[i, j] = newpix[j + embeddede_image.size[1] * i]

embeddede_image.save("HAMMING.bmp")
embeddede_image.close()