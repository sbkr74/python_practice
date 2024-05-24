# Remove punctuations from string
string = "abcd-1234-5678"
a = list(string)
b = []
c = str()
for i in range(len(a)):
    if a[i]=='-':
        continue
    else:
        b.append(a[i])
        c=c+''.join(a[i])
print(c)

# Dynamic input 
a="!@#$%^&*()_+{}:\'\"<>?-=[];,./"
special_chars=list(a)
usr_input = input("Enter a string")
new_string = ""
for char in usr_input:
    if char not in special_chars:
        new_string+=''.join(char)
print(new_string)