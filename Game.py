
Try_again = "YES"
#name = "ROGERs"
#count=len(name)
count = 5
name = ['ROBERT', 'ANDREW', 'ANNET', 'ANGEL', 'PATRICIA']

my_name = []
print("Welcome to the name guessing game")
while count <= 5:
    G_name = input("Gues my name\n")
    if G_name.upper() not in name and count != 0:
        print("Sorry u guessed wrong Try again")
        count -= 1
        print(f"You are left with {count} chances")
    elif G_name.upper() in name and count != 0:

        if G_name.upper() in my_name and count != 0:
            print("You have entered that name alreaady, Choose another name")
            count -= 1
            print(f"You are left with {count} chances")
        else:
            my_name.append(G_name.upper())
            print(my_name)
            if len(my_name) == len(name):
                print("Congragulations you won ")
                break
    elif count == 0:
        print("You have used all your chances ,Try after 24 hours")
        break
