tickets = []

def add_ticket():
    issue = input("Enter issue: ")
    priority = input("Enter priority (Low/Medium/High): ")
    status = "Open"

    ticket = {
        "issue": issue,
        "priority": priority,
        "status": status
    }

    tickets.append(ticket)
    print("Ticket added successfully!")

def view_tickets():
    if len(tickets) == 0:
        print("No tickets found.")
    else:
        for index, ticket in enumerate(tickets, start=1):
            print(f"\nTicket {index}")
            print(f"Issue: {ticket['issue']}")
            print(f"Priority: {ticket['priority']}")
            print(f"Status: {ticket['status']}")

def search_ticket():
    keyword = input("Enter keyword to search: ")

    for ticket in tickets:
        if keyword.lower() in ticket["issue"].lower():
            print(f"Issue: {ticket['issue']}")
            print(f"Priority: {ticket['priority']}")
            print(f"Status: {ticket['status']}")

def update_ticket():
    view_tickets()
    choice = int(input("Select ticket number to update: "))

    new_status = input("Enter new status (Open/In progress/Closed): ")
    tickets[choice - 1]["status"] = new_status

    print("Ticket updated!")

def save_to_file():
    with open("tickets.txt", "w") as file:
        for ticket in tickets:
            file.write(str(ticket) + "\n")

    print ("Tickets saved!")

while True:
    print("\n--- IT Helpdesk Ticket System ---")
    print("1. Add Ticket")
    print("2. View Tickets")
    print("3. Search Ticket")
    print("4. Update Ticket")
    print("5. Save Tickets")
    print("6. Exit")

    choice = input("Choose an option: ")

    if choice == "1":
        add_ticket()
    elif choice == "2":
        view_tickets()
    elif choice == "3":
        search_ticket()
    elif choice == "4":
        update_ticket()
    elif choice == "5":
        save_to_file()
    elif choice == "6":
        print("Goodbye!")
        break
    else:
        print("Invalid option. Please try again.")
