contacts = {}


def add_contact():
    while True:
        user_name = input("Please enter contacts name: ")
        user_number = input("Please enter contacts number: ")

        contacts[user_name] = user_number
        print(f"Contact {user_name} added")
        
        user_exit = input("Do you which to add another number y/n?: ")

        if user_exit == "n":
            break
        else:
            continue
       

def view_contacts():
    if contacts:
        print("\n---Contact List---")
        for name, number in contacts.items():
            print(f"Name: {name} Number: {number}")

    else:
        print("No contacts found")



def search_name():
    
        search = input("Type name you are searching for: ")

        if search in contacts:
            print (f"Name: {search} Number: {contacts[search]}")

        else:
            print(f" {search} does not exist ")


def main_menu():
        while True:
            print("\n--- Contact Book ---")
            print("1. Add New Contact")
            print("2. View All Contacts")
            print("3. Search Contact")
            print("4. Exit")


            choice = input(" Which option would you like to choose ?: ")

            if choice == "1":
                 add_contact()

            elif choice =="2":
                view_contacts()

            elif choice == "3":
                 search_name()

            else:
                 break
            
main_menu()