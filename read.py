import datetime
import operation
def rent_land(data_dict):
    while True:
        key = int(input("Enter the key you want to retrieve: "))
        if key in data_dict:
            value = data_dict[key]
            print(f"Value for key {key}: {value}")

            if value.split(',')[-1].strip() == "Available":
                print("the land is 'Available'")
                Key=str(key)
                user_name = input("Enter your name: ")
                user_age = input("Enter your age: ")
                user_address = input("Enter your address: ")
                user_contact_info = input("Enter your contact information: ")
                rent_month=int(input('enter the no of month you want to rent the land: '))
                cost = value.split(',')[4].strip()
                cost=int(cost)*rent_month
                minute = str(datetime.datetime.now().minute)
                second = str(datetime.datetime.now().second)
                microsecond = str(datetime.datetime.now().microsecond)
                random = minute+second+microsecond
                # Create invoice of land

                invoice_file_name = f"{random}.txt"
                with open(invoice_file_name, 'w') as invoice_file:
                    invoice_file.write("key: ")
                    invoice_file.write(Key)
                    invoice_file.write('\n')
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
                    invoice_file.write("no of month to rent: ")
                    invoice_file.write(str(rent_month))
                    invoice_file.write('\n')
                    invoice_file.write("total cost: ")
                    invoice_file.write(str(cost))
                    invoice_file.write('\n')

                print(f"Invoice created successfully: {invoice_file_name}")

                data_dict[key] = value.rstrip("Available") + "Not Available"
                with open('land_info.txt', 'w') as file:
                 for value in data_dict.values():
                    file.write(value+'\n')
            else:
                print("the land is not 'Available'. Please choose another key.")
                continue  # Ask for key again if land is not available
        else:
            print("Invalid key. Please enter a valid key.")
            continue  # Ask for key again if key is invalid
        break  # Break the loop if a valid key with available land is entered

