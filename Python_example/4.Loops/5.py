# generate a series having square of every +ve integer upto input

print("Generate a sequence of square numbers upto n.")
while True:
    num = input("Enter a number: ")
    if num.isdigit():
        num = int(num)
        break
    else:
        print("Input only accept digits.")

for i in range(1,num+1):
    print(i*i,end=" ")