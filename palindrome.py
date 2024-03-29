def palindrome():
    s=input("Enter string : ")
    if s==s[::-1]:
        print(s,"is a palindrome")
    else:
        print(s,"is not a palindrome")
        
print("=====Palindrome checker=====")
    
palindrome()

#added