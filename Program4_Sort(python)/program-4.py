#Write a Python program to store first year percentage of students in array. Write function for sorting array of floating point numbers in ascending order using
#1. Selection Sort
#2. Bubble sort and display top five scores.

#Selection sort is a sorting method in which numbers are sorted one by one by arranging them in order

#Bubble sort is a sorting method in which numbers are swapped to sort untill no swaps are required

def selection_sort(numbers):
    i=0
    while i<len(numbers):
        j=i
        while j<len(numbers):
            number=numbers[i]
            if number>numbers[j]:
                numbers[i]=numbers[j]
                numbers[j]=number
                j=i
            else:
                j=j+1
        i=i+1
    return numbers

def bubble_sort(numbers,i=0):
    while i+1<len(numbers):
        number=numbers[i]
        if number>numbers[i+1]:
            numbers[i]=numbers[i+1]
            numbers[i+1]=number
            numbers=bubble_sort(numbers)
        else:
            i=i+1
    return numbers

def get_list():
    size=int(input("Enter the size of list:"))
    numbers=[]
    for i in range(size):
        number=int(input(f"Enter the number {i+1}:"))
        numbers.append(number)
    return numbers

def main():
    print("Welcome to sorting program")
    print("Enter corresponding integer as choice to select sorting type\n1.To perform selection sort\n2.To perform Bubble sort\n3.Exit")
    while True:
        choice=int(input("Enter your choice:"))
        if choice==1:
            numbers=get_list()
            print("Unsorted list:",numbers)
            sorted_numbers=selection_sort(numbers)
            print("Sorted list:",sorted_numbers)
        elif choice==2:
            numbers=get_list()
            print("Unsorted list:",numbers)
            sorted_numbers=bubble_sort(numbers)
            print("Sorted list:",sorted_numbers)
        elif choice==3:
            exit(0)
        else:
            print("Invalid input")
    return 0

main()