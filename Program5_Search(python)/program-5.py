#Write a Python program to maintain club members, sort on roll numbers in ascending order.
#Write function “Ternary Search” to search whether particular student is member of club or not. 

# Ternary search is modified binary search that divides array into 3 halves instead of two.
# Mid1=L+(R-L)/3
# Mid2=R-(R-L)/3

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

def ternary_search(sorted_numbers,number,L=0,R=0):
    mid1=int(L+((R-L)/3))
    mid2=int(R-((R-L)/3))
    if sorted_numbers[mid1]==number:
        return mid1
    elif sorted_numbers[mid2]==number:
        return mid2
    elif sorted_numbers[L]==number:
        return L
    elif sorted_numbers[R-1]==number:
        return R-1
    elif number<sorted_numbers[L]:
        return -1
    elif number>sorted_numbers[R-1]:
        return -1
    elif sorted_numbers[mid1]>number:
        value=ternary_search(sorted_numbers,number,L,mid1)
        return value
    elif sorted_numbers[mid2]<number:
        value=ternary_search(sorted_numbers,number,mid2,R)
        return value
    else:
        value=ternary_search(sorted_numbers,number,mid1,mid2)
        return value

def get_list():
    size=int(input("Enter the size of list:"))
    numbers=[]
    for i in range(size):
        number=int(input(f"Enter the number {i+1}:"))
        numbers.append(number)
    return numbers

def main():
    print("Welcome to ternary search")
    numbers=get_list()
    print("Numbers are ",numbers)
    sorted_numbers=selection_sort(numbers)
    print("Sorted numbers are",sorted_numbers)
    print("Enter any character to exit program")
    while True:
        try:
            number=int(input("Enter the number to be searched:"))
        except:
            exit(0)
        else:
            position=ternary_search(sorted_numbers,number,0,len(sorted_numbers))
            if position==-1:
                print("The number does not exist in list")
            else:
                print(f"The position of number is {position+1}")
main()