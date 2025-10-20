import os
import sys
screen_width = 100


def main_menu():
    os.system("cls" if os.name == "nt" else "clear")
    print(f"""
    ----------------------------------------
    |                                      |
    |      Put the fries in the bag        |
    |                                      |
    |                                      |
    |                Play                  |
    |              Controls                |
    |                Quit                  |
    ----------------------------------------
    """)
    x = input("> ").lower()
    if x in ("play", "p", "pl", "pla"):
        os.system("cls" if os.name == "nt" else "clear")
        map_selection()
    elif x in ("controls", "c", "co", "con", "cont", "contr", "contro", "control"):
        control_menu()
    elif x in ("quit", "q"):
        sys.exit()
    else:
        main_menu()

def control_menu():
    os.system("cls" if os.name == "nt" else "clear")
    print("""
    ..................................
    .            Controls:           .
    .                                .
    .         W - Move up            .
    .         A - Move left          .
    .         S - Move down          .
    .         D - Move right         .
    .         P - Pick up item       .
    .         ! - Reset map          .
    .                                .
    ..................................
    """)
    input("Press Enter to go back to the main menu...")
    main_menu()

def map_selection():
    print("""
    ..................................
    .                                .
    .                                .
    .                                .
    .          type you map          .
    .                                .
    .                                .
    .                                .
    .                                .
    .                                .
    ..................................
    """)
    theInput = input("type yo map name or else: ")
    os.system("dir /b /a-d *.txt")
    #mapList = os.system("dir /b /a-d *.txt")

if __name__ == "__main__":
    main_menu()