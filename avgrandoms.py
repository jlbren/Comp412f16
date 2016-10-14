import functools
import random

myfile = 'myrandoms.txt'
file = open(myfile, 'w+')
for i in range(0, 100):
    x = random.randint(0, 100)
    file.write(str(x)+'\n')

file.seek(0)


numList = []
for line in file:
    numList.append(int(line.strip()))

file.close

print(len(numList))
avg = functools.reduce(lambda x, y: int(x) + int(y), numList) / len(numList)
print(avg)
