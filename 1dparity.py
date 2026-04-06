def add_parity(data_bits):
    count_ones = data_bits.count('1') 
    if count_ones % 2 == 0:
        parity = '0'
    else:
        parity ='1' # Even parity
    return data_bits + parity
def check_parity(received):
    return received.count('1') % 2 == 0
data = '1011001'
with_parity = add_parity(data)
print(f'Data with parity bit: {with_parity}')
print(f'No error: {check_parity(with_parity)}')