
import random
import string


class User:
    def __init__(self, user_id, name, password):
        self.details = (user_id, name, password)

    def show_details(self):
        print("User ID:", self.details[0])
        print("Name:", self.details[1])
        print("Password:", self.details[2])


def generate_password(words):
    password = "".join(words) 
   
    password += random.choice(string.digits)
    password += random.choice(string.punctuation)
    password += random.choice(string.ascii_uppercase)

   
    while len(password) < 8:
        password += random.choice(string.ascii_letters + string.digits + string.punctuation)

    return "".join(random.sample(password, len(password))) 


user_id = input("Enter User ID: ")
name = input("Enter Name: ")
words = input("Enter some words (space separated): ").split()

password = generate_password(words)

u = User(user_id, name, password)
u.show_details()
