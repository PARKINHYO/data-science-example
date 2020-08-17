from sys import argv
def sample(l):
    l.pop(0)
    print(sum(list(map(lambda x : int(x), l))))

if __name__ == '__main__':
    sample(argv)



