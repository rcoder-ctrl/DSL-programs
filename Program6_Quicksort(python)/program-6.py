#Write a Python program to store first year percentage of students in array.
# Write function for sortingarray of floating point numbers in ascending order using Quick Sort.

#Quicksort is a sorting method in which we break list around one value known as pivot and arrange list according to it.

def quick_sort(numbers):
    pivot=numbers[0]
    for i in range(len(numbers)):
        