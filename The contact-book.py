"""
Command-line Contact Book
Stores contacts as a list of dictionaries: {"name": ..., "phone": ..., "email": ...}
"""

contacts = []


def add_contact():
    """Prompt the user for details and append a new contact dictionary."""
    name = input("Enter name: ").strip()
    phone = input("Enter phone: ").strip()
    email = input("Enter email: ").strip()

    contact = {"name": name, "phone": phone, "email": email}
    contacts.append(contact)
    print(f"\n✅ Contact '{name}' added successfully!\n")


def search_contact(name):
    """Search contacts by name (case-insensitive). Returns the dict or None."""
    for contact in contacts:
        if contact["name"].lower() == name.lower():
            return contact
    return None


def delete_contact(name):
    """Remove a contact by name. Returns True if deleted, False if not found."""
    contact = search_contact(name)
    if contact:
        contacts.remove(contact)
        return True
    return False


def view_all():
    """Display all contacts in a formatted table."""
    if not contacts:
        print("\n📇 No contacts saved yet.\n")
        return

    print("\n" + "=" * 55)
    print(f"{'NAME':<20}{'PHONE':<15}{'EMAIL':<20}")
    print("-" * 55)
    for c in contacts:
        print(f"{c['name']:<20}{c['phone']:<15}{c['email']:<20}")
    print("=" * 55 + "\n")


def print_menu():
    print("=== Contact Book Menu ===")
    print("1. Add Contact")
    print("2. Search Contact")
    print("3. Delete Contact")
    print("4. View All Contacts")
    print("5. Exit")


def main():
    while True:
        print_menu()
        choice = input("Choose an option (1-5): ").strip()

        if choice == "1":
            add_contact()

        elif choice == "2":
            name = input("Enter name to search: ").strip()
            result = search_contact(name)
            if result:
                print(f"\n🔎 Found: {result['name']} | {result['phone']} | {result['email']}\n")
            else:
                print(f"\n❌ No contact found with name '{name}'.\n")

        elif choice == "3":
            name = input("Enter name to delete: ").strip()
            if delete_contact(name):
                print(f"\n🗑️  Contact '{name}' deleted.\n")
            else:
                print(f"\n❌ No contact found with name '{name}'.\n")

        elif choice == "4":
            view_all()

        elif choice == "5":
            print("\nGoodbye! 👋")
            break

        else:
            print("\n⚠️  Invalid choice. Please enter a number from 1 to 5.\n")


if __name__ == "__main__":
    main()
