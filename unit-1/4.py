# 3. Write a program to enter marks of 4 subjects and display result (result  shall include total, percentage and grade)
numbers = []

print("Enter 10 numbers:")
for i in range(10):
    n = int(input())
    numbers.append(n)

print("armstrong numbers are")
for num in numbers:
    digits = str(num)
    power = len(digits)
    total = 0

    for d in digits:
        total += int(d) ** power

    if total == num:
        print(num)
