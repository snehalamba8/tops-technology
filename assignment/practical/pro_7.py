a = input("Enter main string: ")
b = input("Enter sub string: ")


found =  False

for i in range(len(a) - len(b) + 1):
    match = True
    for j in range(len(b)):
        if a[i + j] != b[j]:
            match = False
            break
    if match:
        found = True
        break

print("Sublist found?", found)
