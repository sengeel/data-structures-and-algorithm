# Big O Notation is used to measure how running time or space requirements for your program grows as input size grows


# LINEAR TIME
def get_squared_numbers(numbers):
    squared_numbers = []
    for n in numbers:
        squared_numbers.append(n*n)
    
    return squared_numbers



brain = get_squared_numbers([2, 5, 8, 9])
print(brain)

# CONSTANT TIME
def find_first_pe(prices, eps, index):
    pe = prices[index]/eps[index]
    return pe

# QUADRATIC TIME
numbers = [3,6,2,4,3,6,8,9]

for i in range(len(numbers)):
    for j in range(i+1, len(numbers)):
        if numbers[i] == numbers[j]:
            print(f"{numbers[i]} is a duplicate")
            break


heros = ['spider man', 'thor', 'hulk', 'iron man', 'captain america']


print(len(heros))
heros.append('black panther')

print(heros)

heros.remove('black panther')
heros.insert(3, 'black panther')
print(heros)

heros[1:3] = ['doctor strange']
print(heros)

heros.sort()
print(heros)



       






 