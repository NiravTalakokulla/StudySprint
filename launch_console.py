print("Welcome to the Launch Console!")
user = input("What is your name? ")
print(f"Hi {user}!")
running = True

while running == True:
    number = input("Pick the numbers 1,2,3 or 4: ")
    if number == "1":
        print("About me: My name is Nirav Talakokulla and I hope to be a robotics engineer in the future")
        print("About Me: Press 1     My Goals: Press 2    My favorite project: Press 3     Exit: Press 4")
    elif number == "2":
        print("My goals are to be able to successfully get a intership in Code2College as well as getting into UT Austin for school")
        print("About Me: Press 1     My Goals: Press 2    My favorite project: Press 3     Exit: Press 4")
    elif number == "3":
        print("My favorite project I've done is create a hand controlled robot car I named the 'Motion Rover' ")
        print("About Me: Press 1     My Goals: Press 2    My favorite project: Press 3     Exit: Press 4")
    elif number == "4":
        print("Bye!")
        running = False

