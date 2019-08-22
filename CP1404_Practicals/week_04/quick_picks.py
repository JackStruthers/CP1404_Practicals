import random
PICKS_PER_LINE = 6
MIN_PICK = 1
MAX_PICK = 45
number_of_picks = int(input("How many quick picks? "))

for i in range(number_of_picks):
    quick_picks = []
    for j in range(PICKS_PER_LINE):
        random_pick = random.randint(MIN_PICK, MAX_PICK)
        while random_pick in quick_picks:
            random_pick = random.randint(MIN_PICK, MAX_PICK)
        quick_picks.append(random_pick)
    quick_picks.sort()
    print(quick_picks)
