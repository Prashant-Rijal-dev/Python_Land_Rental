def read_file_into_dictionary(file_path):   # function that converts the lines from txt in dictoinary
    data_dict = {}
    with open(file_path, 'r') as file:
        line_number = 1
        for line in file:
            data_dict[line_number] = line.strip()
            line_number += 1
    return data_dict

def print_data(data_dict):
    print("key,Kittal no,Location,direction,anna,price,status")
    for key, value in data_dict.items():
        print()
        print(key, value)#prints the data stored in the txt file with a key
        print()
