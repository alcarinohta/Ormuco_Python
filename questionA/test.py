from overlap import overlaped
import random

#Test overlaped function with integer random numbers
print('Integer overlap test')
#Generate a list of integer random numbers
numbers = [random.randrange(1, 100, 1) for i in range(4)]
#Pass the numbers of the list as parameters to the function overlaped
result = overlaped(numbers[0], numbers[1], numbers[2], numbers[3])
#Print the result
print('Is Overlaping? ', str(result))


#Test overlaped function with float random numbers
print('Float overlap test')
#Generate a list of float random numbers
numbers = [random.random() for i in range(4)]
#Pass the numbers of the list as parameters to the function overlaped
result = overlaped(numbers[0], numbers[1], numbers[2], numbers[3])
#Print the result
print('Is Overlaping? ', str(result))