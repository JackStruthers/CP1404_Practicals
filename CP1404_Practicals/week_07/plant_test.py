from week_07.plant_class import Plant


def main():
    plant_name = input("Plant Name: ")
    plant_height = float(input("Plant Height: "))
    plant_growth_rate = float(input("Plant Growth Rate: "))
    plant_details = Plant(plant_name, plant_height, plant_growth_rate)

    plant_details.water(5)

    print(plant_details)


main()
