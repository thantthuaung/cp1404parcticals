HEXADECIMAL_COLOUR = {"WISTERIA": "#c9a0dc",
                      "XANADU": "#738678",
                      "YELLOW ORANGE": "#ffae42",
                      "WINE": "#722f37",
                      "WINTERGREEN DREAM": "#56887d",
                      "WILD STRAWBERRY": "#ff43a4",
                      "WHEAT": "#f5deb3",
                      "VIVID BURGUNDY": "#9f1d35",
                      "VENETIAN RED": "#c80815",
                      "ULTRAMARINE": "#3f00ff"}
user_input = input("Enter Color Name: ").upper()
while user_input != "":
    try:
        print(HEXADECIMAL_COLOUR[user_input])
    except KeyError:
        print("Invalid Input.")
    user_input = input("Enter Color Name: ").upper()
print("Finished")
