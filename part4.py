# Write a Python function called max_num()to find the maximum of three numbers.

def max_num(a,b,c):
    return max([a,b,c])

print(max_num(1,2,3))
print(max_num(100,50,1))
print(max_num(15,30,2))

# Write a Python function called mult_list() to multiply all the numbers in a list.

def mult_list(list):
    #if empty list, return 0
    if len(list) == 0:
        return 0
    prod = list[0]

    if len(list) > 1:
        for i in list[1:]:
            prod = prod * i

        return prod

print(mult_list([1,2,3]))
print(mult_list([]))
print(mult_list([15]))

# Write a Python function called rev_string() to reverse a string.


# Write a Python function called num_within() to check whether a number falls in a given range.


# Write a Python function called pascal() that prints out the first n rows of Pascal's triangle.