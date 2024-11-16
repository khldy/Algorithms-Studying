names = ["Youssef", "Merve", "Joe", "Merve Nur", "anyone", "laila"]
numbers = ["12344", "13424", "1234", "43124", "24542", "2424"]

name = input('Please Enter the name you are searching for: ')

for i in range(len(names)):
    if name == names[i]:
        print('The number is: ', numbers[i])
        break

else: print('Not found')

