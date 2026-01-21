def is_armstrong(num):
    digits = str(num)
    power = len(digits)
    total = sum(int(digit) ** power for digit in digits)
    return total == num

numbers = []
print("Enter 10 numbers:")
for i in range(10):
    numbers.append(int(input()))

armstrong_numbers = [num for num in numbers if is_armstrong(num)]

print("Armstrong numbers are:")
for num in armstrong_numbers:
  print(num)
