# Railway Ticket
print("New Passenger Details \n\n")
name = input("Name: ")
age = input("Age: ")
date_of_journey = input("Date of Journey: ")
train_number = input('Train Number: ')
coach_number = input('Coach Number: ')
seat_number = input('Seat Number: ')

def print_ticket():
    print('**************************************************************')
    print('----------------------- Railway Ticket -----------------------')
    print('**************************************************************')
    print('Date of Journey: '+ date_of_journey+'\t\t\t'+'Train Number: '+train_number)
    print('Name: '+name+'\t\t\t\t'+'Coach Number: '+coach_number)
    print('Age: '+age+'\t\t\t\t\t'+'Seat Number : '+seat_number)
    print('**************************************************************')

def print_seat_number():
    print(seat_number)

print_ticket()
print_seat_number()
