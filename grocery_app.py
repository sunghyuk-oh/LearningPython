shopping_lst = []


class Store:
    def __init__(self, store, address):
        self.store = store
        self.address = address
        self.item_list = []

    def add_shopping_list(self, item):
        self.item_list.append(item)


class Item:
    def __init__(self, title, price, quantity):
        self.title = title
        self.price = price
        self.quantity = quantity


while True:
    choice = int(input("""
  Please choose the option:
  1. Add a shopping list
  2. Display the list
  3. Quit
  """))

    if choice == 1:
        store_name = input('Please enter the store name: ')
        store_address = input('Please enter the store address: ')

        store = Store(store_name, store_address)

        more_choice = input(
            "\nDo you want to add grocery items to the particular shopping list? (yes/no) ")

        if more_choice.lower() == "yes":
            while True:
                item_name = input("\nPlease enter the name of the item: ")
                price = input("Please enter the price of the item: ")
                quantity = input("Please enter the quantity: ")

                item = Item(item_name, price, quantity)
                store.add_shopping_list(item)

                print(f"\n{item_name} has saved to the list!")

                option = input("\nDo you want to add more items? (yes/no) ")
                if option.lower() == "yes":
                    continue
                else:
                    break
        else:
            continue

        shopping_lst.append(store)

    elif choice == 2:
        print("-----------------------------")
        for i in range(len(shopping_lst)):
            print(shopping_lst[i].store)
        print("-----------------------------")

        name_option = input("Enter the store name to display the item list: ")
        print(f"\nThe grocery items for {name_option} are:")
        for i in range(len(shopping_lst)):
            if name_option == shopping_lst[i].store:
                for item in shopping_lst[i].item_list:
                    print(f" - {item.title}")

    elif choice == 3:
        print("Thank you for using the grocery app!")
        break

    else:
        print("You typed the wrong number. Please Try again")
