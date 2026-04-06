def parity_2d(matrix):
    result = []
    for row in matrix:
        result.append(row + [row.count(1) % 2])
        col_parities = [sum(col) % 2 for col in zip(*result)]
        result.append(col_parities)
    return result
