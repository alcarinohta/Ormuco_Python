# Question A

## The Problem
  Your goal for this question is to write a program that accepts two lines (x1,x2) and (x3,x4) on the x-axis and returns whether they overlap. As an example, (1,5) and (2,6) overlaps but not (1,5) and (6,8).

## The Solution
  A function called `overlaped()` was created to check if two lines overlap. It will gets four numbers, separate them in two arrays and sort them. After that it will makes the follwing verification: `if (arr1[1] < arr2[0]) or (arr2[1] < arr1[0])` if this condition is true, it will returns false, that means that the lines don't overlap, otherwise it will returns true, that means that the lines overlap.
The function can be found in the file `overlap.py` in the questionA folder.

## The Test
  A program to test the solution was created `test.py`. Where four random numbers will be generated and passed as paramenters to `overlaped` function and it will prints the values of each line and if overlap is true or false. There are two tests, one to verify integer numbers and the other one to verifiy float numbers. In the terminal run `python test.py`
