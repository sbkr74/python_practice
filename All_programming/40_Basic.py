# String palindrome

# using functions
usr_in = input("Enter a string: ")
rev_str = usr_in[::-1]
if(usr_in == rev_str):
    print(usr_in,'is palindrome as',rev_str)
else:
    print(usr_in,'is not palindrome as',rev_str)