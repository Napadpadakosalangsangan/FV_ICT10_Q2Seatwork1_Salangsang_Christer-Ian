from pyscript import display, document

# List of club members
members = [
    "Peter Quill",
    "Peter Parker",
    "Peter Pan",
    "Peter Griffin",
    "Peter Pettigrew"
]

def verification(e):
    
    # Get the first and last names
    Fname = document.querySelector("#Fname").value.strip()
    Lname = document.querySelector("#Lname").value.strip()

    # Combine the names
    name = (Fname + " " + Lname).title()

    # Store the possible messages in a list
    result = [
        f"Sorry, {name}. Your name is not on the list.",
        f"Congratulations, {name}! You are now part of the ICT club."
    ]

    # Count how many times the name appears. If included - returns 1. If not, - returns 0
    list_check = members.count(name)

    # Convert the comparison result into an integer (1 > 0) - True, (0 > 0) - False
    result_picking = int(list_check > 0)

    # Display the appropriate message
    document.querySelector("#result").innerText = result[result_picking]
