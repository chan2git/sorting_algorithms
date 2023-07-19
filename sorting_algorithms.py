import random

################################################################### BUBBLE SORT ###################################################################

"""
Bubble Sort works by checking if the value at list current index is greater than the value to it's right (list current index + 1)
    If yes, then it will swap the values between those two indexes
    If no, the current index is moved to the next position and repeats the check

The algorithm will continue to iterate until it arrives to the base case where all checks for list current index is greater than list index + 1
    In this base case, the list has been successfully sorted
"""

### Create a function that accepts a list and sorts it by bubble sort
def bubble_sort(list):
    # Establish the index length of the list. Without subtracting 1, you would incorrectly store the number of items/characters found in a given list
    index_length = len(list) - 1
    sorted = False

    # While list is unsorted, continue to loop through algorithm
    while sorted == False:
        sorted = True                                                       # var sorted is flipped to True to break the while loop if base case is achieved, otherwise it will be reassigned false in the nested for loop

        # For loop that will increment the index position for each iteration check
        for i in range(0, index_length):                                  
            if list[i] > list[i+1]:                                         
                list[i], list[i+1] = list[i+1], list[i]                     # If condition is true, swap item in position index with item in position index+1
                sorted = False                                              # If condition is true, reassign False to var sorted, which will keep the outer While loop running for the next iteration check
    return list

### Generates a list of 10 random numbers between 1 to 100, applies bubble_sort(), and prints the sorted list
random_list = random.sample(range(1, 100), 10)
sorted_list = bubble_sort(random_list)
print(f"Bubble Sort: {sorted_list}")




################################################################## SELECTION SORT ##################################################################

"""
Selection Sort works by establishing index 0 in a list as a min value
    This min value is then checked against the next items in subsuquent indexes
    If the checked item is lower in value that the min value, that checked item becomes the new min value
    
The position of min value and current index position is swapped, which sorts the min value to the left of the list
Once the unsorted list only has one item left in index, the list will be successfully sorted
"""

### Create a function that accepts a list and sorts it by selection sort
def selection_sort(list):
    # Establish the index length of the list. Without subtracting 1, you would incorrectly store the number of items/characters found in a given list
    index_length = len(list) - 1

    # Outer For Loop establishes that index i is the min value during each iteration
    for i in range(index_length):
        min_value = i

        # Inner For Loop compares if item at j is less then min value; if true then assign j as the new min value
        for j in range(i+1, len(list)):                                     
            if list[j] < list[min_value]:
                min_value = j

        # Swap item at position 
        list[min_value], list[i] = list[i], list[min_value]

    return list


random_list = random.sample(range(1, 100), 10)
sorted_list = selection_sort(random_list)
print(f"Selection Sort: {sorted_list}")











################################################ FOOTNOTES ################################################

#############################
# Version:    1.00          #
# Date:       07/18/2023    #
# Coder:      CH @chan2git  #
#############################

################################################
# Learning Resources/Guides                    #
# https://www.youtube.com/watch?v=4CykZVqBuCw  # 
# https://www.youtube.com/watch?v=kZH0vWXs_Bk  #
# ChatGPT                                      #
#                                              #
################################################