def main():
    names = ["frank", "jack", "yas", "bob"]
    ages = [15, 8, 20, 9]
    oldest_person = find_oldest_person(names, ages)
    print(oldest_person)


def find_oldest_person(names, ages):
    oldest_position = 0
    for i in range(len(ages)):
        if ages[i] > ages[i - 1]:
            oldest_position = i

    return names[oldest_position]


main()
