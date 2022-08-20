# Section 7: Concluding Project

# take input of the number 'n'
n = int(input())

# loop from 1 to 'n'
ans = []
for i in range(1, n+1):
    current_entry = ''

    # check for divisibility condition
    if i % 3 == 0:
        current_entry = current_entry + 'Fizz'
    if i % 5 == 0:
        current_entry = current_entry + 'Buzz'

    # check if the number is not divisible by either
    if len(current_entry) == 0:
        current_entry = str(i)

    # add entry to answer list
    ans.append(current_entry)

# print answer list
print(ans)	