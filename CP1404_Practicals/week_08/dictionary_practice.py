NAME_TO_AGE = {"Bill": 21, "Jane": 34, "Sven": 56}


def main():
    print(find_names_older_than_threshold(30))


def find_names_older_than_threshold(threshold):
    names_above_threshold = []
    for name, age in NAME_TO_AGE.items():
        if age >= threshold:
            names_above_threshold.append(name)
    return names_above_threshold


main()
