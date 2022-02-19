        
# MY VERSION OF CODE

# # output using f-strings makes the code much more readable
# print(f"Your band name could be {city} {pet_name}.")

# #1. Create a greeting for your program.
# print("Welcome to Band Name Generator!")

# #2. Ask the user for the city that they grew up in.
# city_name = input("What is the city you grew up in?\n")

# #3. Ask the user for the name of a pet.
# pet_name = input("What is the name of your pet?\n")

# #4. Combine the name of their city and pet and show them their band name.
# print("Your band name might be: " + city_name + " " + pet_name)

# --------------------------------------------------------------------------------

# Band Name Generator

print("Welcome to the Band Name Generator.")

# initialize the variables as empty strings
city = ""
pet_name = ""

# simple check to make sure the user has entered something
while True:
    print("What's the name of the city you grew up in?")
    city = input("> ")
    # if there's no input, ask again
    if city == "":
        print("You haven't entered anything. Please try again.")
    # if there's any input at all, break out of the loop
    else:
        break

# do the same for the pet name
while True:
    print("What's your pet's name?")
    pet_name = input("> ")
    if pet_name == "":
        print("You haven't entered anything. Please try again.")
    else:
        break
        

