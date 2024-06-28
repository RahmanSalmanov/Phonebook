class Contact:
    def __init__(self, name, phone_number):
        self.name = name
        self.phone_number = phone_number

    def update_phone_number(self, new_phone_number):
        self.phone_number = new_phone_number

    def __str__(self):
        return f'Name: {self.name}, Phone: {self.phone_number}'


class Phonebook:
    def __init__(self):
        self.contacts = []

    def add_contact(self, contact):
        self.contacts.append(contact)

    def search_contact(self, name):
        for contact in self.contacts:
            if contact.name.lower() == name.lower():
                return contact
        return None

    def display_contacts(self):
        if not self.contacts:
            print("Phonebook is empty.")
        else:
            print("Contacts in Phonebook:")
            for contact in self.contacts:
                print(contact)

# Create a phonebook instance
phonebook = Phonebook()

# Example usage with user inputs
while True:
    print("\nSelect an option:")
    print("1. Add a new contact")
    print("2. Search for a contact")
    print("3. Display all contacts")
    print("4. Exit")

    choice = input("Enter your choice (1/2/3/4): ")

    if choice == '1':
        name = input("Enter contact's name: ")
        phone_number = input("Enter contact's phone number: ")
        new_contact = Contact(name, phone_number)
        phonebook.add_contact(new_contact)
        print(f"{name} added to the phonebook.")

    elif choice == '2':
        search_name = input("Enter the name to search: ")
        found_contact = phonebook.search_contact(search_name)
        if found_contact:
            print("Contact found:")
            print(found_contact)
        else:
            print(f"No contact found with the name '{search_name}'.")

    elif choice == '3':
        phonebook.display_contacts()

    elif choice == '4':
        print("Exiting the phonebook.")
        break

    else:
        print("Invalid choice. Please enter a valid option (1/2/3/4).")
