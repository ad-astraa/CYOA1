def start_game():
    print("Welcome to the Rapunzel Adventure Game!")
    print("You are a brave adventurer who has heard tales of a maiden trapped in a tower.")
    print("Your goal is to find and rescue her. Make your choices wisely!")

    first_decision()

def first_decision():
    print("\nYou arrive at the tower. You can:")
    print("1. Climb the tower using the vines.")
    print("2. Call out to Rapunzel and ask her to let down her hair.")
    
    choice = input("What will you do? (1 or 2): ")

    if choice == "1":
        climb_tower()
    elif choice == "2":
        call_rapunzel()
    else:
        print("Invalid choice. Please choose 1 or 2.")
        first_decision()

def climb_tower():
    print("\nYou decide to climb the tower using the vines. It's a tough climb, but you make it to the top.")
    print("You enter the tower through the window and see Rapunzel.")
    inside_tower()

def call_rapunzel():
    print("\nYou call out, 'Rapunzel, Rapunzel, let down your hair!'")
    print("Rapunzel lets down her long golden hair, and you climb up.")
    inside_tower()

def inside_tower():
    print("\nInside the tower, you can:")
    print("1. Talk to Rapunzel.")
    print("2. Explore the tower for another way out.")
    
    choice = input("What will you do? (1 or 2): ")

    if choice == "1":
        talk_to_rapunzel()
    elif choice == "2":
        explore_tower()
    else:
        print("Invalid choice. Please choose 1 or 2.")
        inside_tower()

def talk_to_rapunzel():
    print("\nYou talk to Rapunzel and learn about her life in the tower.")
    print("She tells you about the witch who keeps her captive.")
    escaping_tower()

def explore_tower():
    print("\nYou decide to explore the tower. You find a hidden passage behind a bookshelf.")
    print("The passage leads to a secret staircase going down.")
    escaping_tower()

def escaping_tower():
    print("\nIt's time to escape the tower. You can:")
    print("1. Use Rapunzel's hair to climb down.")
    print("2. Use the secret staircase you found.")
    
    choice = input("What will you do? (1 or 2): ")

    if choice == "1":
        use_hair()
    elif choice == "2":
        use_staircase()
    else:
        print("Invalid choice. Please choose 1 or 2.")
        escaping_tower()

def use_hair():
    print("\nYou and Rapunzel use her hair to climb down the tower.")
    print("Just as you reach the ground, the witch arrives!")
    print("You confront the witch, and with Rapunzel's help, you manage to escape.")
    happy_ending()

def use_staircase():
    print("\nYou and Rapunzel use the secret staircase to escape the tower.")
    print("As you reach the bottom, you find a secret exit that leads to the forest.")
    print("You and Rapunzel make your way to freedom.")
    happy_ending()

def happy_ending():
    print("\nCongratulations! You successfully rescued Rapunzel and escaped the tower.")
    print("You both live happily ever after.")
    play_again()

def play_again():
    choice = input("\nWould you like to play again? (yes or no): ")

    if choice.lower() == "yes":
        start_game()
    elif choice.lower() == "no":
        print("Thanks for playing! Goodbye.")
    else:
        print("Invalid choice. Please choose yes or no.")
        play_again()

# Start the game
start_game()
