#Write a Python program to store marks scored in subject “Fundamental of Data Structure” by Nstudents in the class.
#Write functions to compute following: 
# a) The average score of class 
# b) Highest score and lowest score of class 
# c) Count of students who were absent for the test 
# d) Display marks with highest frequency

#Arrays don't exist in python.The data structure list is used as an array in python.The only difference between them is list doesn't have fixed size.
#Therefore this program uses list to simulate work of an array

def getdata():
    number_of_students=int(input("Enter the total number of students:"))
    marks_of_students=[]
    i=0
    while i<number_of_students:
        marks=int(input(f"Enter marks of student {i+1}:"))
        if marks>100 or marks<-1:
            print("invalid input,please try again")
        else:
            marks_of_students.append(marks)
            i=i+1
    return number_of_students,marks_of_students

def average_score(present_students,marks_of_students):
    addition=0
    if present_students==0:
        return 0
    for i in range(len(marks_of_students)):
        if marks_of_students[i]==-1:
            pass
        else:
            addition=addition+marks_of_students[i]
    return addition/present_students

def highest_and_lowest_score(present_students,marks_of_students):
    marks=[]
    for i in range(len(marks_of_students)):
        if marks_of_students[i]==-1:
            pass
        else:
            marks.append(marks_of_students[i])
    highest_score=marks[0]
    lowest_score=marks[0]
    i=0
    j=0
    while i<len(marks):
        if highest_score<marks[i]:
            highest_score=marks[i]
            i=0
        else:
            i=i+1
    while j<len(marks):
        if lowest_score>marks[j]:
            lowest_score=marks[j]
            j=0
        else:
            j=j+1
    return highest_score,lowest_score

def absent_students(present_students,number_of_students):
    return number_of_students-present_students

def highest_frequency_marks(present_students,marks_of_students):
    frequencies={}
    i=0
    while i<len(marks_of_students):
        frequency_value=marks_of_students[0]
        frequency=0
        for j in range(len(marks_of_students)):
            if marks_of_students[j]==frequency_value:
                frequency=frequency+1
        frequencies[frequency_value]=frequency
        marks_of_students= [ k for k in marks_of_students if k!=frequency_value]
    del frequencies[-1]
    frequency_list=list(frequencies.values())
    largest_value=frequency_list[0]
    while i<len(frequency_list):
        if largest_value<frequency_list[i]:
            largest_value=frequency_list[i]
            i=0
        else:
            i=i+1
    frequency_value_list=[key for key, value in frequencies.items() if value == largest_value]
    return largest_value,frequency_value_list

def main():
    print("Welcome to student information program")
    print("Enter value -1 for absent students")
    number_of_students,marks_of_students=getdata()
    present_students=0
    for i in range(len(marks_of_students)):
        if marks_of_students[i]==-1:
            pass
        else:
            present_students=present_students+1
    print("Enter values according to operation\n1 : Average score \n2 : Highest and lowest score\n3 : Absent students\n4 : Highest frequency marks\n5 : Exit")
    while True:
        choice=int(input("Enter value for choice:"))
        if choice==1:
            average=average_score(present_students,marks_of_students)
            print("Average score of class is ",average)
        elif choice==2:
            highest,lowest=highest_and_lowest_score(present_students,marks_of_students)
            print("Highest score in class is ",highest)
            print("Lowest score in class is ",lowest)
        elif choice==3:
            absent=absent_students(present_students,number_of_students)
            print("Number of absent students is ",absent)
        elif choice==4:
            frequency,frequency_value=highest_frequency_marks(present_students,marks_of_students)
            print("Marks with Highest frequency are ",frequency_value,":",frequency,"times")
        elif choice==5:
            exit(0)
        else:
            print("Invalid intput")
    return 0

main()