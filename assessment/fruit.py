fruit_list = []

def view_fruits():
    if len(fruit_list) == 0:
        print("No fruits available")
    else:
        for i in range(len(fruit_list)):
            f = fruit_list[i]
            print(i+1, f["name"], "-", f["qty"], "kg - ₹", f["price"])

while True:
    print("\n1) Manager")
    print("2) Customer")
    print("3) Exit")
    role = input("Choose role: ")

    # MANAGER
    if role == "1":
        print("\n1) Add fruit")
        print("2) View stock")
        choice = input("Enter choice: ")

        if choice == "1":
            name = input("Fruit name: ")
            qty = int(input("Quantity (kg): "))
            price = int(input("Price per kg: "))
            fruit_list.append({"name": name, "qty": qty, "price": price})
            print("Fruit added successfully")

        elif choice == "2":
            view_fruits()

    # CUSTOMER
    elif role == "2":
        view_fruits()
        if len(fruit_list) > 0:
            num = int(input("Enter fruit number: ")) - 1
            qty = int(input("Enter quantity: "))

            if qty <= fruit_list[num]["qty"]:
                total = qty * fruit_list[num]["price"]
                fruit_list[num]["qty"] -= qty
                print("Total Bill: ₹", total)
            else:
                print("Not enough stock")

    # EXIT
    elif role == "3":
        print("Thank you!")
        break



