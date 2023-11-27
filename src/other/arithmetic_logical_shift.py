n = -1
for i in range(20):
    print(n)
    n <<= 1

while n < -1:
    print(n)
    n >>= 1