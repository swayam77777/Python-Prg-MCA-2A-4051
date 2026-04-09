from functools import reduce

numbers=[1,2,3,4,5,6,7,8,9,10]

squares=list(map(lambda x:x*x,numbers))
print("squares using map():",squares)

even_numbers=list(filter(lambda x:x%2 == 0 ,numbers))
print("even numbers using filter():",even_numbers)

total_sum=reduce(lambda a, b: a+b,numbers)
print("sum using reduce():",total_sum)
