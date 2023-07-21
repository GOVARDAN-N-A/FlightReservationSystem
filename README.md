# Flight Reservation System
The Flight Reservation System is a simple Python program that allows passengers to sign up, sign in, book tickets, and cancel tickets. Additionally, cashiers can approve or cancel pending ticket requests. The system is designed to be a text-based interface and provides basic functionalities for flight ticket management.

Getting Started
Prerequisites
To run the Flight Reservation System, you need to have Python installed on your machine.


# Run the "flight_reservation.py" file to start the system:
python flight_reservation.py


# Features
Passenger Sign Up: New passengers can create an account by providing their name, password, and age. Each passenger is assigned a unique ID upon successful sign-up.

Passenger Sign In: Existing passengers can sign in using their assigned ID and password to access their account.

Ticket Booking: Signed-in passengers can book tickets by specifying their ID and the number of tickets they wish to book. The system will add the ticket request to the pending list.

Ticket Cancellation: Passengers can cancel their pending ticket requests by providing their ID and the number of tickets they want to cancel.

Ticket Approval: Cashiers can approve pending ticket requests by entering the passenger's ID and the number of tickets to approve. The system will update the ticket status to "Approved" and decrement the total available ticket count.

Ticket Availability Check: Passengers can check the number of available tickets before booking.

# Usage
Upon running the program, you will be presented with a text-based interface showing the main menu.

Choose either the "Passenger" or "Cashier" option to access the respective functionalities.

If you select "Passenger," you can sign up, sign in, book tickets, cancel tickets, and check ticket availability.

If you select "Cashier," you can approve or cancel pending ticket requests.

Follow the prompts to perform actions such as sign-up, sign-in, booking, cancellation, and approval of tickets.

# Contributing
This is a basic implementation and may have room for improvement. Contributions are welcome! Feel free to open issues for bug reports or enhancement requests. If you'd like to contribute code, please fork the repository and create a pull request with your changes.
