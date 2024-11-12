''' 
Problem statement
Given a number N, print sum of all even numbers from 1 to N.
'''

number = int(input())

def sum_of_all_even_nums_till_n(number):
    total_sum = 0
    for i in range(number + 1):  # Include 'number' in the range
        if i % 2 == 0:           # Check if 'i' is even
            total_sum += i
    return total_sum

print(sum_of_all_even_nums_till_n(number))
