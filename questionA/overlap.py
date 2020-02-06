#Overlaping Function Ormuco's Technical Python Assessment 
#Author: Bruna Luisa do Amaral da Silva

# Function to verify if two arrays of two numbers overlap
# Defining the start and the end of each list
def overlaped(v1, v2, v3, v4):

    # Crating the first array with the numbers that will be stored in variables v1 and v2
    arr1 = [v1, v2]
    arr1.sort()

    # Crating the second array with the numbers that will be stored in variables v2 and v3
    arr2 = [v3, v4]
    arr2.sort()
    
    #Print the values stored in each array as line 1 and line 2
    print('line 1 = ', arr1)
    print('line 2 = ', arr2)
    
    # Check if the lines (arrays) overlap.
    # Example: Line 1 [1, 3] and Line 2 [3, 6]
    # If 3 < 3 or 6 < 1 it it will returns false, that means the lines don't overlap
    # Otherwise it will returns true, that means the lines overlap
    if (arr1[1] < arr2[0]) or (arr2[1] < arr1[0]):
        return False
    else:
        return True
