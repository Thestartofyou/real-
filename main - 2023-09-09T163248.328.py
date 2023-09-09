import csv

# Define the CSV file where the data will be stored
CSV_FILE = 'address_book.csv'

# Initialize the address book as an empty list
address_book = []

# Load existing contacts from the CSV file
def load_contacts():
    try:
        with open(CSV_FILE, 'r', newline='') as file:
            reader = csv.reader(file)
            for row in reader:
                address_book.append({'Name': row[0], 'Phone Number': row[1], 'Address': row[2], 'City/State/ZIP Code': row[3]})
    except FileNotFoundError:
        pass

# Save the current contacts to the CSV file
def save_contacts():
    with open(CSV_FILE, 'w', newline='') as file:
        writer = csv.writer(file)
        for contact in address_book:
            writer.writerow([contact['Name'], contact['Phone Number'], contact['Address'], contact['City/State/ZIP Code']])

# Add a new contact to the address book
def add_contact():
    name = input("Enter the name: ")
    phone_number = input("Enter the phone number: ")
    address = input("Enter the address: ")
    city_state_zip = input("Enter the City/State/ZIP Code: ")
    contact = {'Name': name, 'Phone Number': phone_number, 'Address': address, 'City/State/ZIP Code': city_state_zip}
    address_book.append(contact)
    save_contacts()
    print("Contact added successfully!")

# Search for a contact by name
def search_contact():
    search_name = input("Enter the name to search for: ")
    found_contacts = [contact for contact in address_book if search_name.lower() in contact['Name'].lower()]
    
    if found_contacts:
        print("Found contacts:")
        for contact in found_contacts:
            print(f"Name: {contact['Name']}")
            print(f"Phone Number: {contact['Phone Number']}")
            print(f"Address: {contact['Address']}")
            print(f"City/State/ZIP Code: {contact['City/State/ZIP Code']}")
            print()
    else:
        print("No contacts found with that name.")

# List all contacts in the address book
def list_contacts():
    if address_book:
        print("Contacts in the address book:")
        for contact in address_book:
            print(f"Name: {contact['Name']}")
            print(f"Phone Number: {contact['Phone Number']}")
            print(f"Address: {contact['Address']}")
            print(f"City/State/ZIP Code: {contact['City/State/ZIP Code']}")
            print()
    else:
        print("Address book is empty.")

# Main menu
def main_menu():
    load_contacts()
    while True:
        print("\nAddress Book Menu:")
        print("1. Add Contact")
        print("2. Search Contact")
        print("3. List Contacts")
        print("4. Exit")
        choice = input("Enter your choice: ")
        
        if choice == '1':
            add_contact()
        elif choice == '2':
            search_contact()
        elif choice == '3':
            list_contacts()
        elif choice == '4':
            print("Exiting Address Book.")
            break
        else:
            print("Invalid choice. Please try again.")

if __name__ == "__main__":
    main_menu()
