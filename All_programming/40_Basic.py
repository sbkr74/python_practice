# String palindrome
usr_in = input("Enter a string: ")
usr_in = usr_in.casefold()
# using functions
rev_fun = (reversed(usr_in))
if list(usr_in) == list(rev_fun):
    print("palindrome")
else:
    print("not palindrome")

# using reversed index
rev_str = usr_in[::-1]
if(usr_in == rev_str):
    print(usr_in,'is palindrome as',rev_str)
else:
    print(usr_in,'is not palindrome as',rev_str)