class Star_Cinema:
    __hall_list = []

    def entry_hall(self, hallObject):
        self.__hall_list.append(hallObject)

    @property
    def list_of_hall(self):
        return self.__hall_list

class Hall(Star_Cinema):
    def __init__(self, rows, cols, hall_no):
        self.rows = rows
        self.cols = cols
        self.hall_no = hall_no
        self.show_list = []
        self.seats = {}
        super().__init__()


    def entry_show(self, show_id, movie_name, time):
        show_info = (show_id, movie_name, time)
        self.show_list.append(show_info)

        seat = []
        for i in range(self.rows):
            row = []
            for j in range(self.cols):
                row.append('0')
            seat.append(row)
        self.seats[show_id] = seat


    def book_seats(self, show_id, seat_list):
        for show in self.show_list:
            if show[0] == show_id:
                for row, col in seat_list:
                    if row >= 0 and row < self.rows and col >= 0 and col < self.cols:
                        if self.seats[show_id][row][col] == '0':
                            self.seats[show_id][row][col] = '1'
                            print(f"\nYou have successfully booked the seat {row},{col}!!")
                        else:
                            print(f"The seat {row},{col} already booked!!")
                    else:
                        print(f"\nThe seat {row}, {col} does not exists!!\n")
                return
        print(f"\nThe movie with ID {show_id} does not exists in the lsit!!\n")


    def view_show_list(self):
        print("Show List\n---------------------------------------------------------------")
        for show in self.show_list:
            print(f"Movie ID: {show[0]}  Movie Name: {show[1]} \tShow Time: {show[2]}")
        print("---------------------------------------------------------------")


    def view_availabe_seats(self, show_id):
        for show in self.show_list:
            if show[0] == show_id:
                seat = self.seats[show_id]

                for row in seat:
                    print(row)
                return
        
        print(f"\nThe show you searched with ID {show_id} is not in our show list!!\n")


hall1 = Hall(5, 6, 3)
movie = Star_Cinema()
movie.entry_hall(hall1)

hall1.entry_show("10001", "Spiderman", "19/01/2024, 11:00 AM")
hall1.entry_show("10002", "Superman", "19/01/2024, 3:00 PM")
hall1.entry_show("10003", "Iron man", "19/01/2024, 6:30 PM")

current_hall = hall1

while True:

    print("\n1. VIEW ALL SHOW TODAY")
    print("2. VIEW AVAILABLE SEATS")
    print("3. BOOK TICKETS")
    print("4. EXIT")

    option = int(input("\nEnter an option: "))

    if option < 1 or option > 4:
        print("\nOption not valid!! Try again with a valid option.\n")

    if option == 1:
        for show in movie.list_of_hall:
            show.view_show_list()

    elif option == 2:
        hall_id = input("\nEnter movie ID: ")
        current_hall.view_availabe_seats(hall_id)

    elif option == 3:
        id = input("Enter Show ID: ")
        num_of_tickets = int(input("Enter number of Tickets: "))
        ticket_list = []

        for i in range(num_of_tickets):
            r = int(input("Enter seat row: "))
            c = int(input("Enter seat column: "))
            
            tp = (r,c)
            ticket_list.append(tp)
            
        current_hall.book_seats(id, ticket_list)

    elif option == 4:
        break

# for show in hall1.show_list:
#     print(show[0])

# for hall in movie.__hall_list:
#     print(hall.rows, " ", hall.cols, " ", hall.hall_no)