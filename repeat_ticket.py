new_passenger = input("New Passenger Details yes / no: ")
while new_passenger == 'yes':
    new_passenger = input('Enter yes / no to continue')
    if new_passenger == 'yes':
        name = input("Name: ")
        age = input("Age: ")
        date_of_journey = input("Date of Journey: ")
        train_number = input('Train Number: ')
        coach_number = input('Coach Number: ')
        seat_number = input('Seat Number: ')
        print('**************************************************************')
        print('----------------------- Railway Ticket -----------------------')
        print('**************************************************************')
        print('Date of Journey: '+ date_of_journey+'\t\t\t'+'Train Number: '+train_number)
        print('Name: '+name+'\t\t\t\t'+'Coach Number: '+coach_number)
        print('Age: '+age+'\t\t\t\t\t'+'Seat Number : '+seat_number)
        print('**************************************************************')
    elif new_passenger == 'no':
        print('Welcome back!')
        break
    else:
        print('bye')