
scores = []

for i in range(5):
    score = float(input("input score : "))
    scores.append(score)

average = sum(scores) / len(scores)

print(f"{average:.2f}")