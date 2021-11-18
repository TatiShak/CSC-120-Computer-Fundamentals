LetterD = {}
UserString = input("Enter a string: ")
UserString = UserString.upper()
for i in UserString:
    if i.isalpha():
        LetterD[i] = UserString.count(i)
print("Dictionary:", LetterD)

UserChoice = input("Choose a letter: ")
UserChoice = UserChoice.upper()
if UserChoice in LetterD:
    print("Frequency count of that letter: ", LetterD[UserChoice])
    del LetterD[UserChoice]
    print("Dictionary after that letter removed:", LetterD)
else:
    print("The letter", UserChoice, "is not in the dictionary.")

Letters = sorted(LetterD.keys())
print("Letters sorted:", Letters)

