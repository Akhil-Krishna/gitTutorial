def palindrome():
    s=input("Enter string : ")
    if s==s[::-1]:
        print("yes palindrome")
    else:
        print("No its not")
palindrome()