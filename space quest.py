def start_space_adventure():
    print("You are the captain of a spaceship exploring the galaxy. You can:")
    print("1. Visit a nearby planet")
    print("2. Investigate a strange signal")
    print("3. Check the spaceship's status")

    choice = input("What do you want to do? (Enter 1, 2, or 3): ")

    if choice == "1":
        visit_planet()
    elif choice == "2":
        investigate_signal()
    elif choice == "3":
        check_status()
    else:
        print("Invalid choice. Please try again.")
        start_space_adventure()

def visit_planet():
    print("You decide to visit a nearby planet. Upon landing, you see alien life forms.")
    print("Do you want to:")
    print("1. Communicate with the aliens")
    print("2. Collect samples")

    choice = input("What do you want to do? (Enter 1 or 2): ")

    if choice == "1":
        communicate_aliens()
    elif choice == "2":
        collect_samples()
    else:
        print("Invalid choice. Please try again.")
        visit_planet()

def investigate_signal():
    print("You decide to investigate the strange signal. It leads you to a derelict spaceship.")
    print("Do you want to:")
    print("1. Board the spaceship")
    print("2. Scan the spaceship from a distance")

    choice = input("What do you want to do? (Enter 1 or 2): ")

    if choice == "1":
        board_spaceship()
    elif choice == "2":
        scan_spaceship()
    else:
        print("Invalid choice. Please try again.")
        investigate_signal()

def check_status():
    print("You check the spaceship's status. All systems are functioning normally.")
    print("Do you want to:")
    print("1. Continue your journey")
    print("2. Perform maintenance")

    choice = input("What do you want to do? (Enter 1 or 2): ")

    if choice == "1":
        continue_journey()
    elif choice == "2":
        perform_maintenance()
    else:
        print("Invalid choice. Please try again.")
        check_status()

def communicate_aliens():
    print("You communicate with the aliens and establish a friendly relationship.")

def collect_samples():
    print("You collect samples and discover new forms of life.")

def board_spaceship():
    print("You board the derelict spaceship and find valuable resources.")

def scan_spaceship():
    print("You scan the spaceship and detect no signs of life.")

def continue_journey():
    print("You continue your journey through the galaxy.")

def perform_maintenance():
    print("You perform maintenance and ensure the spaceship is in top condition.")

# Start the space adventure
start_space_adventure()
