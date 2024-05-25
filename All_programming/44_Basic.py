# count number of each vowel
vowel = ['a','e','i','o','u']
string = "I am a python developer"
string_list = list(string.lower())
for item in vowel:
    count = 0 
    for ele in string_list:
        if item == ele:
            count+=1
            # print(item,count)
    print(item,count)        

#################################################
vowels = 'aeiou'
string = string.casefold()

# make a dictionary with each vowel a key and value 0
count = {}.fromkeys(vowels,0)

for char in string:
    if char in count:
        count[char] +=1
print(count)

###################################################