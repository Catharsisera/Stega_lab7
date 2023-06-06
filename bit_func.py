"""преобразование числа в двоичное представление"""
def to_bits(numb):
    binary_list = []
    while len(binary_list) < 8:
        numb, bit = divmod(numb, 2)
        binary_list.append(bit)
    binary_list = binary_list[::-1]     #переворот списка для правильного порядка битов
    return binary_list

"""преобразование битового представления в байтовое"""
def to_bytes(lst):
    byte_list = []
    for i in range(0, len(lst), 8):
        bits = lst[i:i + 8]
        byte_value = 0
        for n, bit in enumerate(bits):
            byte_value += 2 ** (7 - n) * bit
        byte_list.append(byte_value)
    return bytes(byte_list)