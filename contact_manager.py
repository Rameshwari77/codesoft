import json
import os

CONTACTS_FILE = 'contacts.json'

# --------------------- Helper Functions ---------------------
def load_contacts():
    if os.path.exists(CONTACTS_FILE):
        with open(CONTACTS_FILE, 'r') as f:
            return json.load(f)
    return []

def save_contacts(contacts):
    with open(CONTACTS_FILE, 'w') as f:
        json.dump(contacts, f, indent=2)

def display_contacts(contacts):
    if not contacts:
        print("No contacts found.")
        return
    print("\n--- Contact List ---")
    for idx, contact in enumerate(contacts, 1):
        print(f"{idx}. {contact['name']} | {contact['phone']}")

def find_contact(contacts, keyword):
    results = []
    for contact in contacts:
        if keyword.lower() in contact['name'].lower() or keyword in contact['phone']:
            results.append(contact)
    return results

# --------------------- CRUD Operations ---------------------
def add_contact(contacts):
    name = input("Enter name: ")
    phone = input("Enter phone number: ")
    email = input("Enter email: ")
    address = input("Enter address: ")
    
    contacts.append({
        'name': name,
        'phone': phone,
        'email': email,
        'address': address
    })
    print("Contact added successfully.")

def search_contact(contacts):
    keyword = input("Enter name or phone number to search: ")
    results = find_contact(contacts, keyword)
    if results:
        print("\n--- Search Results ---")
        for contact in results:
            print_contact_details(contact)
    else:
        print("No matching contacts found.")

def print_contact_details(contact):
    print(f"\nName: {contact['name']}")
    print(f"Phone: {contact['phone']}")
    print(f"Email: {contact['email']}")
    print(f"Address: {contact['address']}")

def update_contact(contacts):
    keyword = input("Enter name or phone of contact to update: ")
    results = find_contact(contacts, keyword)
    if not results:
        print("No matching contact found.")
        return
    contact = results[0]
    print("Leave blank to keep current value.")

    new_name = input(f"New name [{contact['name']}]: ") or contact['name']
    new_phone = input(f"New phone [{contact['phone']}]: ") or contact['phone']
    new_email = input(f"New email [{contact['email']}]: ") or contact['email']
    new_address = input(f"New address [{contact['address']}]: ") or contact['address']

    contact.update({
        'name': new_name,
        'phone': new_phone,
        'email': new_email,
        'address': new_address
    })
    print("Contact updated successfully.")

def delete_contact(contacts):
    keyword = input("Enter name or phone of contact to delete: ")
    results = find_contact(contacts, keyword)
    if not results:
        print("No matching contact found.")
        return
    contact = results[0]
    print_contact_details(contact)
    confirm = input("Are you sure you want to delete this contact? (y/n): ").lower()
    if confirm == 'y':
        contacts.remove(contact)
        print("Contact deleted.")
    else:
        print("Delete operation canceled.")

# --------------------- Main Program ---------------------
def main():
    contacts = load_contacts()

    while True:
        print("\n=== Contact Manager ===")
        print("1. View Contacts")
        print("2. Add Contact")
        print("3. Search Contact")
        print("4. Update Contact")
        print("5. Delete Contact")
        print("6. Exit")

        choice = input("Select an option (1-6): ")

        if choice == '1':
            display_contacts(contacts)
        elif choice == '2':
            add_contact(contacts)
        elif choice == '3':
            search_contact(contacts)
        elif choice == '4':
            update_contact(contacts)
        elif choice == '5':
            delete_contact(contacts)
        elif choice == '6':
            save_contacts(contacts)
            print("Contacts saved. Goodbye!")
            break
        else:
            print("Invalid choice. Try again.")

if __name__ == "__main__":
    main()
