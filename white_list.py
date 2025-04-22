admin = "ianek"
white_list = [] 
black_list = []

while True:
    request = input("What is your name: ")
    print(f"Received request: {request}")  # Debugging statement (chatgpt helped)
    
    if request in black_list:
        print("you have been black listed you are not welcome")
        continue # Skip further checks for this user
    
    #only the admin gets this prompt
    if request == admin:
        interaction = input("would you like to white list, black list or remove some one: ").lower()

        #adds people to the white list list
        if interaction == "white list":
            Wadd = input("Who would you like to whitelist: ")
            white_list.append(Wadd)
            print(f"{Wadd} has been whitelisted.")   # Debugging statement (chatgpt helped)
            print(f"Current whitelist:{white_list}")  # Debugging statement (chatgpt helped)

        #remove people from the list
        elif interaction == "remove":
            remove = input("who would you like to remove: ")
            white_list.remove(remove)
            print(f"{remove} has been removed from the white list")

        #view the list
        elif interaction == "open list":
            print(f"white list {white_list}")
            print(f"black list {black_list}")

        #black list
        elif interaction == "black list":
            Badd = input("who would you like to black list: ")
            black_list.append(Badd)
            print(f"{Badd} has been black listed")
            print(f"current black list:{black_list}")

    #for the people who arnt in the list
    elif request not in white_list:
        print("You are not whitelisted.")
        print("Ask the admin to whitelist you.")
    
    else:
        print("Welcome!")
