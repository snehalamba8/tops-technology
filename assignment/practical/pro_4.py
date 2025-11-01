#get a single string from two given strings, separatedbya space and swap the first two characters of each string

s1 = input("Enter first string: ")
s2 = input("Enter second string: ")


n_s1= s2[:2] + s1[2:]  #swap first two characters
n_s2= s1[:2] + s2[2:]


result = n_s1 + " " + n_s2  #join with space
print(result)
