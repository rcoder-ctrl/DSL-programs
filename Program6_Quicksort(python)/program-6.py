#Write a Python program to store first year percentage of students in array.
# Write function for sortingarray of floating point numbers in ascending order using Quick Sort.

#Quicksort is a sorting method in which we break list around one value known as pivot and arrange list according to it.

def quick_sort(numbers):
    pivot=numbers[0]
    list1=[]
    list2=[]
    list3=[]
    for i in range(len(numbers)):
        if numbers[i]>pivot:
            list2.append(numbers[i])
        elif numbers[i]<pivot:
            list1.append(numbers[i])
        elif numbers[i]==pivot:
            list3.append(numbers[i])
    if len(list1)>1:
        list1=quick_sort(list1)
    if len(list2)>1:
        list2=quick_sort(list2)
    for i in range(len(list3)):
        list1.append(list3[i])
    for i in range(len(list2)):
        list1.append(list2[i])
    return list1

def get_data():
    size=int(input("Enter the number of values:"))
    numbers=[]
    for i in range(size):
        number=float(input(f"Enter the float value {i+1}:"))
        numbers.append(number)
    return numbers

def main():
    print("Welcome to quicksort")
    print("Enter corresponding choices\n1.To perform quicksort\n2.Exit")
    while True:
        choice=int(input("Enter the choice:"))
        if choice==1:
            numbers=get_data()
            print("The list is ",numbers)
            sorted_numbers=quick_sort(numbers)
            print("Sorted list is ",sorted_numbers)
        elif choice==2:
            exit(0)
        else:
            print("Invalid input")
main()