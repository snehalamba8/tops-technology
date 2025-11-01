#add 'ing' at the end of a given string (length at least 3). If the given string already ends with 'ing
# ' then add 'ly' instead If thestring length of the given string is less than 3, leave it unchanged

text = input("Enter a string: ")

if len(text) >= 3:
    if text.endswith("ing"):
        text = text + "ly"
    else:
        text = text + "ing"

print("Result:", text)


