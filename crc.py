def crc(data, divisor):
    data = data + '0' * (len(divisor) - 1)
    data = list(data)
    for i in range(len(data) - len(divisor) + 1):
        if data[i] == '1':
            for j in range(len(divisor)):
                data[i+j] = str(int(data[i+j]) ^ int(divisor[j]))
    remainder = ''.join(data[-(len(divisor)-1):])
    return remainder
data = '11010011101100'
divisor = '1011'
print(f'CRC Remainder: {crc(data, divisor)}')