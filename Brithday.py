Dict={}
while True:
    print("========== Brithday Adder =============\n")
    print("1. Show the Brithday ")
    print("2.  Add to Brithday in list ")
    print("3. Exit ")
    choice = int(input("Enter the choice\n"))
    if choice == 1:
        if len(Dict) == 0: #If no data in dictionary
            print("Nothing to show !")
        else : #If data is there ask him whose data he want
            name = input("Enter name to look for birthday :")
            birthday = Dict.get(name,"No data found!")
            print (birthday)
    elif choice == 2:  #If he want to add user data let him add in dictionary as key-value pair.
        name = input ("Enter Name :")
        date = input ("Enter Birthdate :")
        Dict[name] = date
        print ("Birthday Added !")
    elif choice == 3: #close program
        print("======Exiting program========")
        break
    else: #if he has chosen none of above input plese ask him to chose valid option
        print("Choose a valid option !")


