import random
elements = []
for i in range(10):
    randm1 = random.randint(1,100)
    randm2 = random.randint(1,100)
    elements.append((randm1, randm2))

print(elements)
maximum = []
for i in range(len(elements)):
    add = elements[i][0] + elements[i][1]
    maximum.append(add)

print(maximum)
maxi = max(maximum)
print(maxi)

for i in range(len(maximum)):
    if maximum[i] == maxi:
        print(f"The pair with the highest sum is {elements[i]} at index {i}")
