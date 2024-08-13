
# ARRAYS

enter_input = int(input('Please enter your number \n'))

odd_numbers =[]

for i in range(1, enter_input):
    if i % 2 != 0:
        odd_numbers.append(i)
        
print(odd_numbers)
