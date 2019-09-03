HEX_COLOURS = {"AliceBlue": "#f0f8ff", "AntiqueWhite": "#faebd7", "aquamarine1": "#7fffd4", "azure1": "#f0ffff",
               "beige": "#f5f5dc", "black": "#000000", "BlanchedAlmond": "#ffebcd", "BlueViolet": "#8a2be2",
               "brown": "#a52a2a", "burlywood": "#deb887"}

colour_choice = input("Please enter the colour you wish to know the code of: ")
while colour_choice != "":
    if colour_choice in HEX_COLOURS:
        print(HEX_COLOURS[colour_choice])
    else:
        print("Invalid colour")
    colour_choice = input("Please enter the colour you wish to know the code of: ")
