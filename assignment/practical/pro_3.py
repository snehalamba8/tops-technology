
text=input("Enter the string::")
lower=text.lower()
split=lower.split()
count={}

#count the words
for i in split:
    if i in count:
        count[i]+=1
    else:
        count[i]=1

#print the words occurrence
for i,count in count.items():
    print(i,count)                