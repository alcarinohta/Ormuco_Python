# Question B

## The Problem
The goal of this question is to write a software library that accepts 2 version string as input and returns whether one is greater than, equal, or less than the other. As an example: “1.2” is greater than “1.1”. Please provide all test cases you could think of.

## The Solution
The function `version_comp` created intends to verify which version is the latest one, when comparing two versions of some software. 
To do do, it will converts the versions numbers or letters in two arrays (splitted by '.' dots), then verifies which version has the greater length and add a zero at the end of the array for the shortest one, that way inside the loop a verification will pass by each position of the arrays (including the zeros added, if needed) return 1 if the version 2 is smaller then version 1, -1 if the version 1 is smaller the version 2 and 0 if the version are equal.

## The Test
The program to test the function `test.py` was created, and it will asks for the user to input two versions to be compared. Then 
it will checks if the number returned from the function is less then zero, greater than zero or equal to zero and the result will be "version 2 is the latest one", "version 1 is the latest one" and "Both versions are equal" respectively.

Run `python test.py` to test it.
