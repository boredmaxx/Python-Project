contacts = {}

def add_contact():
    name = input("Name: ").strip()
    if not name:
        print("Name cannot be empty.")
        return
    
    if name in contacts:
        print("Contact already exists.")
        return
    
    phone = input("Phone: ").strip()
    contacts[name] = {"phone": phone}
    print(f"Contact '{name}' added successfully!")

def update_contact():
    name = input("Name to update: ").strip()
    if name not in contacts:
        print("Contact not found.")
        return
    
    print(f"Current phone: {contacts[name]['phone']}")
    phone = input("New phone (press Enter to keep current): ").strip()
    
    # Keep existing value if user presses Enter
    if phone:
        contacts[name]["phone"] = phone
    
    print(f"Contact '{name}' updated successfully!")

def delete_contact():
    name = input("Name to delete: ").strip()
    if name in contacts:
        confirm = input(f"Are you sure you want to delete '{name}'? (y/n): ").lower()
        if confirm == 'y':
            del contacts[name]
            print(f"Contact '{name}' deleted successfully!")
        else:
            print("Deletion cancelled.")
    else:
        print("Contact not found.")

def search_contact():
    if not contacts:
        print("No contacts available.")
        return
    
    term = input("Search term: ").lower().strip()
    if not term:
        print("Search term cannot be empty.")
        return
    
    found = False
    for name, details in contacts.items():
        if (term in name.lower() or 
            term in details.get("phone", "").lower()):
            print(f"{name}: Phone: {details['phone']}")
            found = True
    
    if not found:
        print("No matching contacts found.")

def view_all_contacts():
    if not contacts:
        print("No contacts available.")
        return
    
    print(f"\n--- All Contacts ({len(contacts)}) ---")
    for name, details in sorted(contacts.items()):
        print(f"{name}: Phone: {details['phone']}")

def main():
    while True:
        print("\n--- Contact Book Menu ---")
        print("1. Add Contact")
        print("2. Update Contact")
        print("3. Delete Contact")
        print("4. Search Contact")
        print("5. View All Contacts")
        print("6. Exit")
        
        choice = input("Enter choice (1-6): ").strip()
        
        if choice == "1":
            add_contact()
        elif choice == "2":
            update_contact()
        elif choice == "3":
            delete_contact()
        elif choice == "4":
            search_contact()
        elif choice == "5":
            view_all_contacts()
        elif choice == "6":
            print("Goodbye!")
            break
        else:
            print("Invalid choice. Please enter a number between 1-6.")

if __name__ == "__main__":
    main()