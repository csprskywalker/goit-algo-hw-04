def parse_input(user_input):
    cmd, *args = user_input.split()
    cmd = cmd.strip().lower()
    return cmd, *args

def add_contact(args, contacts):
    name, phone = args
    contacts[name] = phone
    return "Contact added."

def remove_contact(args, contacts):
    name, phone = args
    del contacts[name]
    return "Contact deleted successfully"

def change_contact(args, contacts):
    name, phone = args
    contacts[name] = phone
    return "Contact changed successfully"

def all_contacts(contacts):
    if not contacts:
        return "No contacts available."
    return '\n'.join(f"{name}: {phone}" for name, phone in contacts.items())

def phone_username(name, contacts):
    if name in contacts:
        return contacts[name]


def main():
    contacts = {}
    print("Welcome to the assistant bot!")
    while True:
        user_input = input("Enter a command: ")
        command, *args = parse_input(user_input)

        if command in ["close", "exit"]:
            print("Good bye!")
            break
        elif command == "hello":
            print("How can I help you?")
        elif command == "add":
            response = add_contact(args, contacts)
            print(response)
            print(f"Current contacts: {contacts}")
        elif command == "del":
            print(remove_contact(args, contacts))
        elif command == "change":
            print(change_contact(args, contacts))
        elif command == "all":
            print(all_contacts(contacts))
        elif command == "pu":
            print(phone_username(args[0], contacts))
        else:
            print("Invalid command.")

if __name__ == "__main__":
    main()
