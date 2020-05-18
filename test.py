import time
a = time.time()
for i in range(1000):
    for j in range(10000):
        k = (-1) ** (i + j)
b = time.time()
print(b - a)

c = time.time()
for i in range(1000):
    for j in range(10000):
        k = -1 if ((i + j) % 2) else 1
d = time.time()
print(d - c)