# Remove punctuations from string
string = "abcd-1234-5678"
string_list = list(string)
b = []
c = str()
for i in range(len(string_list)):
    if string_list[i]=='-':
        continue
    else:
        b.append(string_list[i])
        c=c+''.join(string_list[i])
print(c)
#####################################################
# Dynamic input 
a="!@#$%^&*()_+{}:\'\"<>?-=[];,./"
special_chars=list(a)
usr_input = input("Enter a string")
new_string = ""
for char in usr_input:
    if char not in special_chars:
        new_string+=''.join(char)
print(new_string)
#####################################################
s=""
string = '12#$56&*90!@@(87^%43@!'
new_string_list = list(string)
for ele in new_string_list:
    if ele.isalnum():
        s+=''.join(ele)
print(s)