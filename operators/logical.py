b1 = True
b2 = False

print(not b1)
print(not b2)
print(b1 and b2)
print(b1 or b2)
print(not b1 and b2)
print(b1 != b2) # Equivalente ao XOR

print(not b1 and (not b2 or b1))