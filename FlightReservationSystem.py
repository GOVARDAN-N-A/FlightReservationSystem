class Flight:
    def __init__(self):
        self.passengers = []
        self.tickets = []
        self.id = 1201
        self.ticket_count = 50
        
    def start(self):
        while True:
            print("\n********** FLIGHT RESERVATION SYSTEM **********")
            print("1. Passenger")
            print("2. Cashier")
            print("3. Exit")
            choice = input("Enter Your Choice -> ")
            
            if choice == "1":
                self.passenger_menu()
            elif choice == "2":
                self.cashier_menu()
            elif choice == "3":
                break
            else:
                print("Invalid Choice !")
                
    
    def passenger_menu(self):
        while True:
            print("***** Passenger Menu *****")
            print("1. Sign Up")
            print("2. sign In")
            print("3. Back")
            choice = input("Enter Your Choice -> ")
            
            if choice == "1":
                name = input("Enter Your Name : ")
                password = input("Enter Your Password : ")
                age = input("Enter Your Age : ")
                passenger = {
                    'id' : str(self.id),
                    'name':name,
                    'password':password,
                    'age':age
                }
                self.id += 1
                self.passengers.append(passenger)

                print("Sign Up Successful.\nYour Passenger ID is : ", passenger['id'])
                
            elif choice == "2":
                
                passenger_id = input("Enter Your Passenger ID : ")
                password = input("Enter Your Password : ")
                
                for passenger in self.passengers:
                    if passenger['id'] == passenger_id and passenger['password'] == password:
                        print("Sign In Successful !")
                        while True:
                            print("1. Book Ticket ")
                            print("2. Cancel Ticket")
                            print("3. Check Availablity")
                            print("4. Back")
                            choice = input("Enter Your Choice : ")
                            
                            if choice == "1":
                                
                                pass_id  = input("Enter Your Id :")
                                if pass_id in passenger['id']:
                                    ticket_count = int(input("Enter No of Tickets : "))

                                    ticket = {

                                        'passenger_id':pass_id,
                                        'ticket_count':ticket_count,
                                        'status':'pending'
                                    }

                                    self.tickets.append(ticket)
                                    print("Ticket is waiting for approval...")
                                else:
                                    print("Invalid Id !")
                                
                                
                            elif choice == "2":
                                
                                pass_id  = input("Enter Your Id :")
                                c_t = int(input("No of Tickets to cancel : "))
                                
                                for ticket in self.tickets:
                                    if pass_id == str(ticket['passenger_id']) and ticket['status'] == 'pending':
                                        ticket['status'] = 'Cancelled'
                                        print("Ticket cancelled successfully.")
                                
                            elif choice == "3":
                                print("No of Tickets Available : ",self.ticket_count)
                                
                            elif choice == "4":
                                break
                                
                            else:
                                print("Invalid Choice")
                                
                    else:
                        print("Invalid Id or Password")
                                
            
            elif choice == "3":
                break
            else:
                print("Invalid Choice")
            
                                
    def cashier_menu(self):
        
        while True:
            print("***** Cashier Menu *****")
            print("1. Approve Ticket")
            print("2. Cancel Ticket")
            print("3. Back")
            choice = input("Enter Your Choice : ")
                  
            if choice == "1":
                  
                if not self.tickets:
                    print("No ticket requests found.")
            
                else:
                    for ticket in self.tickets:
                        if ticket['status'] == 'pending':
                            print("Passenger ID", ticket['passenger_id'], "| Ticket Count", ticket['ticket_count'])



                    for ticket in self.tickets:

    #                     if pass_id == ticket['passenger_id'] and ticket['status'] == 'Pending':
                            pass_id = input("Enter pass ID :")
                            no_tickets = int(input("Enter No of Tickets : "))
                            ticket['status'] = 'Approved'
                            self.ticket_count-=no_tickets

                            print("Ticket approved successfully.")
    
            elif choice == "2":
                continue

            elif choice == "3":
                break

                
                
            else:
                print("Invalid Choice")

obj = Flight()
obj.start()


                      




