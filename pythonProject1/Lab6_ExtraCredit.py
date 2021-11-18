s = "i_love_programming_in_python_and_i_will_alzways_program"
letter=[]
for i in s:
    if s.count(i) == 1:
        letter.append(i)
print(letter)
