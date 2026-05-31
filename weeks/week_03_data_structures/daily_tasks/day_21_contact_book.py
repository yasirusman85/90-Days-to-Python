"""
Day 21 Milestone Project: Interactive Contact Book CLI 📞
---------------------------------------------------------
Consolidate lists, dictionaries, parsing loops, and user choices by 
engineering a command-line Contact Book application.

Task Requirements:
1. Store contacts in a list called 'contacts'. Each contact is represented 
   as a dictionary: {"name": str, "phone": str, "email": str}
2. Run the application inside a loop giving the user choices:
   - 1: Add new contact
   - 2: Search contact by name
   - 3: View all contacts
   - 4: Delete a contact
   - 5: Exit
3. Write clean helper functions to handle each choice option.
"""

contacts = []

def add_contact():
    print("\n--- Add Contact ---")
    name = input("Enter Name: ")
    phone = input("Enter Phone: ")
    email = input("Enter Email: ")
    
    # TODO: Create a contact dictionary, append to contacts list, and print success.
    pass

def search_contact():
    print("\n--- Search Contact ---")
    search_name = input("Enter Name to Search: ")
    
    # TODO: Loop through contacts list, find matches, and display.
    pass

def view_all_contacts():
    print("\n--- View All Contacts ---")
    
    # TODO: If contacts is empty, print notification. Else, loop and print each.
    pass

def delete_contact():
    print("\n--- Delete Contact ---")
    delete_name = input("Enter Name to Delete: ")
    
    # TODO: Loop through list, remove matching contact, and print success status.
    pass

def main():
    while True:
        print("\n=== Contact Book CLI ===")
        print("1. Add Contact")
        print("2. Search Contact")
        print("3. View All Contacts")
        print("4. Delete Contact")
        print("5. Exit")
        
        choice = input("Enter choice (1-5): ")
        if choice == "1":
            add_contact()
        elif choice == "2":
            search_contact()
        elif choice == "3":
            view_all_contacts()
        elif choice == "4":
            delete_contact()
        elif choice == "5":
            print("Goodbye! 👋")
            break
        else:
            print("Invalid Choice! Please enter 1-5.")

if __name__ == "__main__":
    main()
