
data = ((0, 1, 2), (3, 4, 5), (6, 7, 8), (9, 10, 11))

data_transpose = [list(i) for i in zip(*data)]
print(data_transpose)