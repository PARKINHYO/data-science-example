import time


print(time.strftime('%Y/', time.localtime(time.time())), end="")
ex = time.strftime('%x', time.localtime(time.time()))
print(ex[:5], end=" ")
print(time.strftime('%X', time.localtime(time.time())))