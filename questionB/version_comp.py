#Version Comparison Ormuco's Technical Python Assessment 
#Author: Bruna Luisa do Amaral da Silva

# The version comparison will returns:
# 1 if the version 2 is smaller then version 1
# -1 if the version 1 is smaller the version 2
# 0 if the version are equal

# The logical used is if the first numbers are greater it means the version is latest
# For example: Version 1 = 1.4.5 and Version 2 = 1.6.1, it means thar Version 2 is the latest one

def version_comp(version1, version2):

    #Create arrays with the versions and then slipt them by dots
    arr1 = version1.split('.')
    arr2 = version2.split('.')
    
    #Length of arr1 - length of arr2 to check the difference between them
    #And follow the correct rule for comparison
    len_dif = len(arr1) - len(arr2)
    
    #Add a 0 to the array with less data
    #So the loop will be able to compare all positions of the arrays
    if len_dif > 0:
        arr2 = arr2 + ["0"]*len_dif
    elif len_dif < 0:
        arr1 = arr1 + ["0"]*(-len_dif)

    #Check each position of each array and compare them
    for counter in range(0, len(arr1)):
        #If arr1 is greater it will return 1
        if arr1[counter] > arr2[counter]:
            return 1
        #If arr2 is greater it will return 1
        elif arr1[counter] < arr2[counter]:
            return -1

    return 0

    
