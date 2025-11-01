

my_list = [11,32,34,34,34,55,67,67,88,99]



def abc(lst):
    u_list = []
    for item in lst:
        if item not in u_list:
            u_list.append(item)
    return u_list

print("Unique list:", abc(my_list))
