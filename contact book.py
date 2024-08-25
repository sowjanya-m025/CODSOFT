contacts = {}

def add_contact():
    name = input("Enter name: ")
    phone = input("Enter phone number: ")
    email = input("Enter email: ")
    address = input("Enter address: ")
    contacts[name] = {'phone': phone, 'email': email, 'address': address}
    print("Contact added successfully.")

def see_contact_list():
    if not contacts:
        print("No contacts found.")
    else:
        print("Contact List:")
        for name, info in contacts.items():
            print(f"Name: {name}, Phone: {info['phone']}")

def search_contact():
    query = input("Enter name or phone number to search: ")
    for name, info in contacts.items():
        if query.lower() in name.lower() or query in info['phone']:
            print(f"Name: {name}")
            print(f"Phone: {info['phone']}")
            print(f"Email: {info['email']}")
            print(f"Address: {info['address']}")
            return
    print("Contact not found.")

def update_contact():
    name = input("Enter name of the contact to update: ")
    if name in contacts:
        phone = input(f"Enter new phone number (current: {contacts[name]['phone']}): ")
        email = input(f"Enter new email (current: {contacts[name]['email']}): ")
        address = input(f"Enter new address (current: {contacts[name]['address']}): ")
        contacts[name] = {'phone': phone, 'email': email, 'address': address}
        print("Contact updated successfully.")
    else:
        print("Contact not found.")

def delete_contact():
    name = input("Enter name of the contact to delete: ")
    if name in contacts:
        del contacts[name]
        print("Contact deleted successfully.")
    else:
        print("Contact not found.")

def main():
    while True:
        print("\nContact Management System")
        print("1. Add Contact")
        print("2. View Contact List")
        print("3. Search Contact")
        print("4. Update Contact")
        print("5. Delete Contact")
        print("6. Exit")

        choice = input("Enter your choice (1-6): ")

        if choice == '1':
            add_contact()
        elif choice == '2':
            view_contact_list()
        elif choice == '3':
            search_contact()
        elif choice == '4':
            update_contact()
        elif choice == '5':
            delete_contact()
        elif choice == '6':
            print("Exiting Contact Management System...")
            break
        else:
            print("Invalid choice. Please try again.")

if __name__ == "__main__":
    main()





