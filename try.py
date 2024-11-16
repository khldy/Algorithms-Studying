numbers = [12, 30, 14, 45, 60 ,9, 16]
target = int(input('Enter the target number:'))

for i in range(len(numbers)):
     if numbers[i] == target:
         print('Target number found at index', i)
         break
else:
    print('Target number not found')