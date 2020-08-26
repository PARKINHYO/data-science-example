from sys import argv
argv.pop(0)
argv = list(map(lambda x : int(x), argv))
print(argv)
