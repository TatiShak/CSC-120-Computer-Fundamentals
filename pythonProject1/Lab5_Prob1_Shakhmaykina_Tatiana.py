import copy

score1 = []
for counter in range(5):
    userscore = int(input("Enter a test score: "))
    score1.append(userscore)
print("All scores:", score1)

score2 = copy.deepcopy(score1)
for counter in range(len(score2)):
    if score2[counter] < 60:
        score2[counter] = score2[counter] + 10
print("Students who scored below 60 get 10 extra points.")
print("All scores:", score2)
print("Students whose scores have changed:")
for counter in range(len(score1)):
    if score1[counter] != score2[counter]:
        print("Old score:", score1[counter], "New score:", score2[counter])
