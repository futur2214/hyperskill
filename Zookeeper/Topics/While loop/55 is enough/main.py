# put your code here
n = int(input())
found = (n == 55)
number = 1
s = n
average = n
while not found:
    n = int(input())
    if n != 55:
        number = number + 1
        s = s + n
    else:
        found = True
average = s / number
average=round(average)
print(number)
print(s)
print(average)
