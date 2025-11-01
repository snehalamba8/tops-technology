
no = list(map(int, input("Enter numbers: ").split()))


if len(no) < 2:
    print("No second smallest number found")
else:
     no.sort()
     print("Second smallest number is:", no[1])
