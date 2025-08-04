import json

contacts = []

def save_contacts():
    with open("contacts.json", "w") as file:
        json.dump(contacts, file)

def load_contacts():
    try:
        with open("contacts.json", "r") as file:
            return json.load(file)
    except FileNotFoundError:
        return []

def add_contact():
    name = input("Enter name: ")
    phone = input("Enter phone number: ")
    email = input("Enter email: ")
    address = input("Enter address: ")
    
    new_contact = {
        "name": name,
        "phone": phone,
        "email": email,
        "address": address
    }
    
    contacts.append(new_contact)
    save_contacts()
    print("Contact added successfully!")

def view_contacts():
    if not contacts:
        print("No contacts found.")
    else:
        for index, contact in enumerate(contacts, start=1):
            print(f"{index}. {contact['name']} - {contact['phone']}")

def search_contact():
    search_term = input("Enter name or phone number to search: ")
    found_contacts = [contact for contact in contacts if search_term.lower() in contact['name'].lower() or search_term in contact['phone']]
    
    if not found_contacts:
        print("No contacts found.")
    else:
        for index, contact in enumerate(found_contacts, start=1):
            print(f"{index}. {contact['name']} - {contact['phone']} - {contact['email']} - {contact['address']}")

def update_contact():
    name = input("Enter name of contact to update: ")
    for contact in contacts:
        if contact['name'].lower() == name.lower():
            contact['phone'] = input(f"Enter new phone number ({contact['phone']}): ") or contact['phone']
            contact['email'] = input(f"Enter new email ({contact['email']}): ") or contact['email']
            contact['address'] = input(f"Enter new address ({contact['address']}): ") or contact['address']
            save_contacts()
            print("Contact updated successfully!")
            return
    print("Contact not found.")

def delete_contact():
    name = input("Enter name of contact to delete: ")
    for contact in contacts:
        if contact['name'].lower() == name.lower():
            contacts.remove(contact)
            save_contacts()
            print("Contact deleted successfully!")
            return
    print("Contact not found.")

def main():
    global contacts
    contacts = load_contacts()
    
    while True:
        print("\n---CONTACT BOOK---")
        print("1. Add Contact")
        print("2. View Contacts")
        print("3. Search Contact")
        print("4. Update Contact")
        print("5. Delete Contact")
        print("6. Exit")
        
        choice = input("Choose an option: ")
        
        if choice == "1":
            add_contact()
        elif choice == "2":
            view_contacts()
        elif choice == "3":
            search_contact()
        elif choice == "4":
            update_contact()
        elif choice == "5":
            delete_contact()
        elif choice == "6":
            print("Goodbye!")
            break
        else:
            print("Invalid choice. Please try again.")

if __name__ == "__main__":
    main()
    