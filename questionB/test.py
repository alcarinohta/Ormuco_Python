from version_comp import version_comp

#Ask for the user to input two versions to be compared
version1 = str(input("please enter a decimal number: "))
version2 = str(input("please enter a 2nd decimal number: "))

#Comparison of the version from user`s input
comp =  version_comp(version1, version2) 
if comp < 0: 
    print (version2, " is the latest version")
elif comp > 0: 
    print (version1, " is the latest version")
else: 
    print ("Both versions are equal")