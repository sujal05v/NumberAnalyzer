# Number Analyzer

"""
 Features:
 > Even / Odd check 
 > Sum of digits 
 > Count Digits 
 > Reverse Number 
 > Palindrome Check 
 > Largest number
 """



n = int(input("Enter Number: "))

# 1. Even / Odd
if n % 2 == 0:
    print("Number is Even:", n)
else:
    print("Number is Odd:", n)


# 2. Sum of Digits
temp = n
sum_digits = 0

while temp > 0:
    digit = temp % 10
    sum_digits += digit
    temp = temp // 10

print("Sum of Digits:", sum_digits)


# 3. Count Digits
temp = n
count = 0

while temp > 0:
    temp = temp // 10
    count += 1

print("Total Digits:", count)


# 4. Reverse Number
temp = n
rev = 0

while temp > 0:
    digit = temp % 10
    rev = rev * 10 + digit
    temp = temp // 10

print("Reverse Number:", rev)


# 5. Palindrome Check
if rev == n:
    print("Number is Palindrome")
else:
    print("Number is not Palindrome")


# 6. Largest Digit
temp = n
largest = 0

while temp > 0:
    digit = temp % 10
    if digit > largest:
        largest = digit
    temp = temp // 10

print("Largest Digit:", largest)