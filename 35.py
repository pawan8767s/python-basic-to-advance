## Find largest number from 1–N ##

n = int(input("Enter N: "))

largest = 1

for i in range(1, n + 1):
    if i > largest:
        largest = i

print("Largest number =", largest)