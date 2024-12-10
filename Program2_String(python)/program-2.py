#Write a Python program to compute following operations on String:
#a) To display word with the longest length
#b) To determines the frequency of occurrence of particular character in the string
#c) To check whether given string is palindrome or not
#d) To display index of first appearance of the substring
#e) To count the occurrences of each word in a given string

#Pallindrome is a word which gives same word after reversing

#python acts on string easily and has many ways to control string by character index

def getdata():
    statement=str(input("Enter the string:"))
    return statement.lower()

def longest_word(statement):                     #for those who didn't want to use split refer function in split_replacement.py
    words=statement.split(' ')
    word=words[0]
    i=0
    while i<len(words):
        if len(words[i])>len(word):
            word=words[i]
            i=0
        else:
            i=i+1
    return word

def character_frequency(sentence):
    character=(str(input("Enter character you want to check:"))).lower()
    frequency=0
    for i in range(len(sentence)):
        if sentence[i]==character:
            frequency=frequency+1
    return frequency

def Pallindrome(sentence):
    sentence_reverse=sentence[::-1]
    if sentence_reverse==sentence:
        return True
    else:
        return False
    
def first_appearence(sentence):
    word=(str(input("Enter the substring:"))).lower()
    for i in range(len(sentence)):
        if word==sentence[i:i+len(word)]:
            return i
    return -1

def word_frequency(sentence):
    words=sentence.split(' ')
    i=0
    while i<len(words):
        count=0
        word=words[0]
        for j in range(len(words)):
            if word==words[j]:
                count=count+1
        print(word,":",count)
        words=[j for j in words if j!=word]
    return 0

def main():
    print("Welcome to string administrator")
    sentence=getdata()
    print("Enter choices as your requirement\n1:To check the longest word in string\n2:To check frequency of given character\n3:To check if given string is pallindrome or not\n4:To check first appearence index of a substring\n5:To check frequency of words in a string\n6:Exit")
    while True:
        choice=int(input("Enter your choice:"))
        if choice==1:
            word=longest_word(sentence)
            print("longest word in statement is",word)
        elif choice==2:
            frequency=character_frequency(sentence)
            print("Frequency of given character is ",frequency)
        elif choice==3:
            value=Pallindrome(sentence)
            if value:
                print("Given string is a Pallindrome")
            else:
                print("Given word is not a Pallindrome")
        elif choice==4:
            index=first_appearence(sentence)
            if index==-1:
                print("word does not exist in the given string")
            else:
                print("index of given string is ",index)
        elif choice==5:
            word_frequency(sentence)
        elif choice==6:
            exit(0)
        else:
            print("Invalid input")
main()