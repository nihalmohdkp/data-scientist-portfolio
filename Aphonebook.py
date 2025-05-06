phone_book = {}

def add_contact():
    name = input("Enter contact name: ")
    phone_number = input("Enter phone number: ")
    phone_book[name] = phone_number
    print(f"Contact {name} added with phone number {phone_number}.")

def update_contact():
    name = input("Enter contact name to update: ")
    if name in phone_book:
        phone_number = input("Enter new phone number: ")
        phone_book[name] = phone_number
        print(f"Contact {name} updated with new phone number {phone_number}.")
    else:
        print("Contact not found.")

def view_contact():
    name = input("Enter contact name to view: ")
    if name in phone_book:
        print(f"{name}: {phone_book[name]}")
    else:
        print("Contact not found.")

def display_all_contacts():
    if phone_book:
        for name, phone_number in phone_book.items():
            print(f"{name}: {phone_number}")
    else:
        print("No contacts in phone book.")

def delete_contact():
    name = input("Enter contact name to delete: ")
    if name in phone_book:
        del phone_book[name]
        print(f"Contact {name} deleted.")
    else:
        print("Contact not found.")

def main():
    while True:
        print("\nPhone Book Menu:")
        print("1. Add Contact")
        print("2. Update Contact")
        print("3. View Contact")
        print("4. Display All Contacts")
        print("5. Delete Contact")
        print("6. Exit")

        choice = input("Enter your choice (1-6): ")

        if choice == '1':
            add_contact()
        elif choice == '2':
            update_contact()
        elif choice == '3':
            view_contact()
        elif choice == '4':
            display_all_contacts()
        elif choice == '5':
            delete_contact()
        elif choice == '6':
            print("Exiting phone book. Goodbye!")
            break
        else:
            print("Invalid choice. Please enter a number between 1 and 6.")

if __name__ == "__main__":
    main()