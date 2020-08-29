#print name function

full_name = input("Enter your first and last name: ")

def print_name(full_name):
    lst = list(full_name.split(" "))
    print(f"First name is: {lst[0]}")
    print(f"Last name is: {lst[1]}")

print_name(full_name)

print("aa")