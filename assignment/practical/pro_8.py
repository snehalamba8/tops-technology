
def contains_sublist(list1, list2):
    
    for i in range(len(list1) - len(list2) + 1):
        if list1[i:i+len(list2)] == list2:
            return True
    return False

main = [1, 2, 3, 4, 5, 6]
sub = [3]

if contains_sublist(main, sub):
    print("Sublist found.")
else:
    print("Sublist not found.")

