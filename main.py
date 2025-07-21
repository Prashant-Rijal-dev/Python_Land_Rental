import operation
import read
import write

print()
print('                          welcome to the land rental management portal')
print()
file_path = 'land_info.txt'  
data_dictionary = operation.read_file_into_dictionary(file_path)
operation.print_data(data_dictionary)
cond=True
while cond==True:
    print()
    print('enter 1 to rent the land')
    print()
    print('enter 2 to return the land')
    print()
    print('enter 3 to exit the land management portal')
    print()
    user_input = input("Enter 1, 2, or 3: ")
    if user_input not in ['1', '2', '3']:
        print("Error: Invalid input. Please enter 1, 2, or 3.")
        continue
    if user_input == '1':
        condi=True
        print()
        print('you have chosen to rent the land')
        print() 
        while condi==True:
            read.rent_land(data_dictionary)
            # You can rent another land
            condition=input('do you want to rent another land if yes enter "yes" if no enter "no"')
            condition.lower()
            if condition=='yes':
                read.rent_land(data_dictionary)
                condi=True
                break
            else:
                condi=False
        cond=True
    elif user_input=='2':
        write.return_land(data_dictionary)
        cond=True
    elif user_input=='3':
        print("you have exited the land management portal")
        cond=False
    
