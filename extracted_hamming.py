from PIL import Image
from bit_func import *

def hamming(cont, metka):
    H = [
        [1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1],
        [0, 1, 1, 0, 0, 1, 1, 0, 0, 1, 1, 0, 0, 1, 1],
        [0, 0, 0, 1, 1, 1, 1, 0, 0, 0, 0, 1, 1, 1, 1],
        [0, 0, 0, 0, 0, 0, 0, 1, 1, 1, 1, 1, 1, 1, 1]
    ]

    buffer = []
    result = None
    i = 0
    while i * 15 < len(cont):   #проверка, что доступ к c_part выполняется только в пределах длины списка cont
        c_part = cont[i*15:(i+1)*15]    #берем по 15 бит из контейнера
        Hc = [sum([(H[r][e] * c_part[e]) % 2 for e in range(15)]) % 2 for r in range(4)]   #вычисляем значения проверочных битов
        buffer.extend(Hc)

        if len(buffer) >= len(metka):
            if buffer[-len(metka):] == metka: #в случае обнаружения метки окончания производится преобразование в байтовую строку и декодирование из кодировки
                result = to_bytes(buffer[:-len(metka)])
                break
        i += 1

    return result.decode('cp1251') if result is not None else ''

metka = []
for i in "hs45*i!88".encode('cp1251'):
    metka.extend(to_bits(i))

image_path = Image.open('HAMMING.bmp')
pix = image_path.load()
pixels = []

for x in range(image_path.size[0]):
    for y in range(image_path.size[1]):
        pixels.extend(pix[x, y])

extracted_mes = hamming(pixels, metka)
print(extracted_mes)

image_path.close()