from PIL import Image
from bit_func import *

def hamming_invert_bits_index(cont):    #поиска индексов битов, которые подверглись инверсии
    H = [
        [1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1],
        [0, 1, 1, 0, 0, 1, 1, 0, 0, 1, 1, 0, 0, 1, 1],
        [0, 0, 0, 1, 1, 1, 1, 0, 0, 0, 0, 1, 1, 1, 1],
        [0, 0, 0, 0, 0, 0, 0, 1, 1, 1, 1, 1, 1, 1, 1]
    ]

    buffer = []

    for i in range(0, 256):     # по 4 бита из сообщения
        c_part = cont[i*15:(i+1)*15]
        Hc = [sum([(H[r][e] * c_part[e]) % 2 for e in range(15)]) % 2 for r in range(4)]
        index = Hc[3] * 8 + Hc[2] * 4 + Hc[1] * 2 + Hc[0]
        buffer.append(index + i * 15)

    return buffer

def lsb(cont, start=0, step=1):
    e = start
    result = []
    while True:
        result.append(cont[e] % 2)
        e += 1
        if len(result) >= len(metka):
            tmp = result[-len(metka):]
            if tmp == metka:
                break
    return to_bytes(result[:-len(metka)]).decode('cp1251')

def lsb3(cont, start=0, step=1):
    e = start
    result = []
    while True:
        result.append((cont[e//3] // 2**(e % 3)) % 2)
        e += 1
        if len(result) == 200:
            print(result)
        if len(result) >= len(metka):
            tmp = result[-len(metka):]
            if tmp == metka:
                break
    return to_bytes(result[:-len(metka)]).decode('cp1251')

metka = []
for i in "hs45*i!88".encode('cp1251'):
    metka.extend(to_bits(i))

print("\bEXTRACTED_LSBr_R3\b")
image_path = Image.open('Embedded_LSBR_R1.bmp')
pix = image_path.load()
pixels = []

for x in range(image_path.size[0]):
    for y in range(image_path.size[1]):
        pixels.extend(pix[x, y])
result = lsb(pixels)
print(result)
image_path.close()

print("\bEXTRACTED_LSBM_R1\b")
image_path = Image.open('Embedded_LSBM_R1.bmp')
pix = image_path.load()
pixels = []

for x in range(image_path.size[0]):
    for y in range(image_path.size[1]):
        pixels.extend(pix[x, y])
result = lsb(pixels)
print(result)
image_path.close()

print("\bEXTRACTED_LSBR_R3\b")
image_path = Image.open('Embedded_LSBR_R3.bmp')
pix = image_path.load()
pixels = []
for x in range(image_path.size[0]):
    for y in range(image_path.size[1]):
        pixels.extend(pix[x, y])
result = lsb3(pixels)
print(result)
image_path.close()

print("\bEXTRACTED_LSBM_R3\b")
image_path = Image.open('Embedded_LSBM_R3.bmp')
pix = image_path.load()
pixels = []

for x in range(image_path.size[0]):
    for y in range(image_path.size[1]):
        pixels.extend(pix[x, y])
result = lsb3(pixels)
print(result)
image_path.close()

print("\bEXTRACTED_LSBR_R0.25\b")
image_path = Image.open('Embedded_LSBR_R1.bmp')
pix = image_path.load()
pixels = []

for x in range(image_path.size[0]):
    for y in range(image_path.size[1]):
        pixels.extend(pix[x, y])
result = lsb(pixels, 0, 4)
print(result)
image_path.close()

print("\bEXTRACTED_LSBM_R0.25\b")
image_path = Image.open('Embedded_LSBM_R1.bmp')
pix = image_path.load()
pixels = []

for x in range(image_path.size[0]):
    for y in range(image_path.size[1]):
        pixels.extend(pix[x, y])
result = lsb(pixels, 0, 4)
print(result)
image_path.close()