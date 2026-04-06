def compute_checksum(data_segments):
    total = sum(int(seg, 2) for seg in data_segments)
 # Add carry bits
    while total > 0xFFFF:
        total = (total & 0xFFFF) + (total >> 16)
    checksum = ~total & 0xFFFF
    return format(checksum, '016b')
segments = ['1001100110011001', '1010101010101010']
cs = compute_checksum(segments)
print(f'Checksum: {cs}')
