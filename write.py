import datetime
def return_land(data_dict):
    print()
    print('you have chosen to return the land')
    print()
    key = int(input("Enter the key of the land you want to return: "))
    while True:
        if key in data_dict:
            value = data_dict[key]
            print(f"Value for key {key}: {value}")
            #check for returnability
            if value.split(',')[-1].strip() == "Not Available":
                print("Last element of value is 'NOt Available' so it is returnable")
                invoice_number=input('enter your invoice number')
                invoice_file_name=f"{invoice_number}.txt"
                invoice_exist = False
                try:
                    with open(invoice_file_name, 'r'):
                        invoice_exist = True
                except FileNotFoundError:
                    print('invoice dosent exist')
                if invoice_exist==True:
                    try:
                        with open(invoice_file_name, 'r') as file:
                            for line in file:
                                if f"key={key}" in line:
                                    invoice_exist=True
                                    return False
                    except FileNotFoundError:
                        print(f"Error: File '{invoice_file_name}' not found.")
                        invoice_exist=False
                        return False
                    if invoice_exist==True:
                        user_name = input("Enter your name: ")
                        user_age = input("Enter your age: ")
                        user_address = input("Enter your address: ")
                        user_contact_info = input("Enter your contact information: ")
                        user_month=float(input('enter the no of month you exceeded in use: '))
                        fine= value.split(',')[4].strip()
                        fine= float(fine)
                        fine=fine*user_month
                        fine=fine*(10/100)
                        minute = str(datetime.datetime.now().minute)
                        second = str(datetime.datetime.now().second)
                        microsecond = str(datetime.datetime.now().microsecond)
                        random = minute+second+microsecond
                        invoice_file_name = f"{random}.txt"
                        with open(invoice_file_name, 'w') as invoice_file:
                                    invoice_file.write("Name: ")
                                    invoice_file.write(str(user_name))
                                    invoice_file.write('\n')
                                    invoice_file.write("Age: ")
                                    invoice_file.write(str(user_age))
                                    invoice_file.write('\n')
                                    invoice_file.write("address: ")
                                    invoice_file.write(str(user_address))
                                    invoice_file.write('\n')
                                    invoice_file.write("contact no: ")
                                    invoice_file.write(str(user_contact_info))
                                    invoice_file.write('\n')
                                    invoice_file.write("no of month exceeded in rent: ")
                                    invoice_file.write(str(user_month))
                                    invoice_file.write('\n')
                                    invoice_file.write("total fine: ")
                                    invoice_file.write(str(fine))
                                    invoice_file.write('\n')
                        print()
                        print('the land is returned')
                        print('the envoice is created ',invoice_file_name)
                        data_dict[key] = value.rstrip("Not Available") + "Available"
                        with open('land_info.txt', 'w') as file:
                            for value in data_dict.values():
                                file.write(value+'\n')
                        
        else:
            print("Invalid key. Please enter a valid key.")
            continue
        break

