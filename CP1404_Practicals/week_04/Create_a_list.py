scores = []
score = int(input("Score:"))
while score >= 0:
    scores.append(score)
    score = int(input("Scores: "))

print("Your highest score is", max(scores))
