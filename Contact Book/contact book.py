contacts = {}

def add_contact(name, phone, email):
    contacts[name] = [phone, email]
    print("Contact added successfully!")

def view_contact(name):
    if name in contacts:
        print("Name:", name)
        print("Phone:", contacts[name][0])
        print("Email:", contacts[name][1])
    else:
        print("Contact not found.")

def update_contact(name, phone, email):
    if name in contacts:
        contacts[name] = [phone, email]
        print("Contact updated successfully!")
    else:
        print("Contact not found.")

def delete_contact(name):
    if name in contacts:
        del contacts[name]
        print("Contact deleted successfully!")
    else:
        print("Contact not found.")

def search_contact(query):
    found = False
    for name, contact in contacts.items():
        if query in name or query in contact:
            print("Name:", name)
            print("Phone:", contact[0])
            print("Email:", contact[1])
            found = True
    if not found:
        print("No matching contacts found.")

def main():
    while True:
        print("\nContact Book")
        print("1. Add Contact")
        print("2. View Contact")
        print("3. Update Contact")
        print("4. Delete Contact")
        print("5. Search Contact")
        print("6. Exit")

        choice = input("Enter your choice: ")

        if choice == '1':
            name = input("Enter name: ")
            phone = input("Enter phone number: ")
            email = input("Enter email address: ")
            add_contact(name, phone, email)
        elif choice == '2':
            name = input("Enter name: ")
            view_contact(name)
        elif choice == '3':
            name = input("Enter name: ")
            phone = input("Enter new phone number: ")
            email = input("Enter new email address: ")
            update_contact(name, phone, email)
        elif choice == '4':
            name = input("Enter name: ")
            delete_contact(name)
        elif choice == '5':
            query = input("Enter name or email to search: ")
            search_contact(query)
        elif choice == '6':
            print("Exit program...")
            break
        else:
            print("Invalid choice. Please enter a number between 1 and 6.")

if __name__ == "__main__":
    main()
