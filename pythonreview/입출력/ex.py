f1 = open("test.txt", "r")
tmp = f1.read()
tmp = tmp.replace("java", "python")
f1.close()

f1 = open("test.txt", "w")
f1.write(tmp)
f1.close()