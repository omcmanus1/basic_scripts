import wikipedia 
import time

### FUNCTIONS ###

def user_choice():
    print("Is this good?\n")
    print("[Y] if you are happy.")
    print("[N] if you want a different one.\n")
    choice = input("> " )
    if choice == "Y":
        print("Here's your link, enjoy.\n")
        show_link()
        print("\n Quitting in 5 seconds...")
        time.sleep(5)
        quit()
    elif choice == "N":
        get_random()
    else:
        print("That wasn't one of the options. Please try again.")
        user_choice()

def get_random():
    global random_page
    random_page = wikipedia.random(pages=1)
    print(random_page + "\n")
    user_choice()

def show_link():
    print(wikipedia.page(random_page).url)

### PROGRAM ###

print("Hello! Here's a random Wikipedia page for you:\n")
get_random()
user_choice()



