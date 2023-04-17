class ParkingGarage():
    def __init__(self):
        self.tickets = ["a ticket"]
        self.parkingSpaces = ["a parking space"]
        self.currentTicket = {"paid":False}
        
    def takeTicket(self):
        self.tickets.pop()
        self.parkingSpaces.pop()

    def payForParking(self):
        payment = input("How much will you pay for your ticket? ")
        if payment:
            print("Your ticket has been paid. You have 15 minutes to leave.")
            self.currentTicket["paid"] = True

    def leaveGarage(self):
        if self.currentTicket["paid"]:
            print("Thank you, have a nice day.")
        else:
            payment = input("You haven't paid for your ticket! How much will you pay? ")
            if payment:
                print("Thank you, have a nice day.")
        
        if self.currentTicket["paid"] or payment:
            self.tickets.append("a ticket")
            self.parkingSpaces.append("a parking space")
            self.currentTicket["paid"] = False

garage = ParkingGarage()
garage.takeTicket()
garage.payForParking()
garage.leaveGarage()