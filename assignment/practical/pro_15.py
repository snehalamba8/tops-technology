


n = int(input("Enter number: "))

a, b = 0, 1
f_series = []

for i in range(n):
    f_series.append(a)
    a, b = b, a + b

print("First few Fibonacci numbers are:", f_series)
