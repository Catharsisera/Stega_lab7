from PIL import Image
from bit_func import *

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
image_path = Image.open('Embedded_LSBR_R0.25.bmp')
pix = image_path.load()
pixels = []

for x in range(image_path.size[0]):
    for y in range(image_path.size[1]):
        pixels.extend(pix[x, y])
result = lsb(pixels, 0, 4)
print(result)
image_path.close()

print("\bEXTRACTED_LSBM_R0.25\b")
image_path = Image.open('Embedded_LSBM_R0.25.bmp')
pix = image_path.load()
pixels = []

for x in range(image_path.size[0]):
    for y in range(image_path.size[1]):
        pixels.extend(pix[x, y])
result = lsb(pixels, 0, 4)
print(result)
image_path.close()