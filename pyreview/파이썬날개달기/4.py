def ex(ex):
    return ex < 0

print(list(filter(ex, [1, -2, 3, -5, 8, -3])))
print(list(map(lambda x : -x, [1, -2, 3, -5, 8, -3])))