# Requires Python 3.10

direction = input("Which direction? ").lower()

match direction:
    case "north":
        print("Up")
    case "south":
        print("down")
    case "east":
        print("right")
    case "west":
        print("left")