names_list = []


for i in range(3):

    name = input("Enter a name: ")

    names_list.append(name)


print("List of names:", names_list)


specific_name = input("Enter a name to check if it's in the list: ")

if specific_name in names_list:

    print(f"{specific_name} is in the list.")

else:

    print(f"{specific_name} is not in the list.")