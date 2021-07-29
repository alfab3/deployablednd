import random

print('Enter your modifier: ')

modifier = input()

print('Enter which dice to roll: ')

x = input()

print('Enter how many times to roll: ')

y = input()

counter = 1
output = 0
for counter in range(y):
        num = random.randint(1,x)
        print num
        output = num + output

output = output + modifier
print output
