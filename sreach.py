strings = ["A7a", "fa4kh", "gedan", "tarsh", "a7a tany", "a7a mogdadan"]

target = input("Enter the word you're searching for: ")
found = False
for i in range(len(strings )):
    if strings[i] == target:
        found = True
print(found)



