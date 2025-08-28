def is_palin():
    s=input("enter a string")
    temp=s
    if s==temp[::-1]:
        print("it is an plaindrome")
    else:
        print("it is not an plaindrome")
    return s
is_palin()
