# # Ask user for name
# name = input("What's your name? ").strip().title()

# # Remove whitespace from string and capitalize name
# # name = name.strip().title()

# # Capitalize name
# # name = name.capitalize()
# # name = name.title()

# # Split user's name into two
# first, last = name.split(" ")

# #Say hello to User
# print(f"Hello, {last}")

# # defining your own functions
# def hello(user="Cod3r"):
#     print("Hello,", user)

# defining main function
def main():
    name = input("What's your name?: ")
    hello(name)

def hello(to="world"):
    print("Hello,", to)


main()