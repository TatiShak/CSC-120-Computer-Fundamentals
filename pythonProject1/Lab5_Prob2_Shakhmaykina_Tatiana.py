intlist = []
choice = "y"
while choice.lower() != "n":
    if choice.lower() == "y":
        userint = int(input("Enter an integer from 1 to 10: "))
        intlist.append(userint)
    choice = input("Enter another integer?[y/n] ")

print("Number list:", intlist)

print("Largest element:", max(intlist))
print("Smallest element:", min(intlist))

sum = 0
for num in intlist:
    sum = sum + num
print("Sum of all elements:", sum)

count = len(intlist)
average = sum/count
print("Length of list:", count)
print("Average:", average)

intlist.reverse()
print("List reversed:", intlist)

intlist.insert(0, intlist[count - 1])
del intlist[len(intlist) - 1]
print("Last element moved to front:", intlist)
