# Write code that loops a for loop over some range 
# and prints how many even numbers are in that range. Try it with:
# range(5)
# range(10)
# range(2,9,3)
# range(-4,6,2)
# range(5,6)

k=0
for i in range(5):
    if i % 2 == 0:
        k += 1
print(k)

k=0
for i in range(10):
    if i % 2 == 0:
        k += 1
print(k)

k=0
for i in range(2,9,3):
    if i % 2 == 0:
        k += 1
print(k)

k=0
for i in range(-4,6,2):
    if i % 2 == 0:
        k += 1
print(k)

k=0
for i in range(5,6):
    if i % 2 == 0:
        k += 1
print(k)