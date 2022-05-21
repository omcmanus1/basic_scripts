import wikipedia 
import time

### FUNCTIONS ###

def user_choice():
    print("Enter [Y] if you want the link.")
    print("Enter [N] if you want a different one.\n")
    choice = input("> " )
    if choice == "Y":
        print("\nHere's your link, enjoy.\n")
        show_link()
        print("\n(Quitting in 5 seconds...)")
        time.sleep(5)
        quit()
    elif choice == "N":
        get_random()
    else:
        print("That wasn't one of the options. Please try again.\n")
        user_choice()

def get_random():
    global random_page
    random_page = wikipedia.random(pages=1)
    print("\n" + "\033[1m" + random_page + "\033[0m" + "\n")
    user_choice()

def show_link():
    random_link = (wikipedia.page(random_page).url)
    print("\033[1m" + "\033[4m" + random_link + "\033[0m" + "\033[0m")

### PROGRAM ###

print("Hello! Here's a random Wikipedia page for you:")
get_random()
user_choice()
