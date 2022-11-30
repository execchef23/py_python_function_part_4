# Write a Python function called max_num()to find the maximum of three numbers.

def max_num(a,b,c):
    return max([a,b,c])

print(max_num(3,5,9))
print(max_num(200,500,12))
print(max_num(150,320,22))

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

print(mult_list([4,7,5]))
print(mult_list([]))
print(mult_list([150]))

# Write a Python function called rev_string() to reverse a string.

def rev_string(my_str):
    return my_str[::-1]

print(rev_string(""))
print(rev_string("happy"))
print(rev_string("bite me"))

# Write a Python function called num_within() to check whether a number falls in a given range.

def num_within(x,a,b):
    return x in range(a,b+1)

print(num_within(6,25,44))
print(num_within(23,23,45))
print(num_within(6,76,35))

# Write a Python function called pascal() that prints out the first n rows of Pascal's triangle.

triangle = [[1],[1,1]]
def pascal(n):
    if n < 1:
        print("invalid number of rows")
    elif n == 1:
        print(triangle[0])
    else:
        row_number = 2

        while len(triangle) < n:
            row = []
            row_prev = triangle[row_number - 1]

            length = len(row_prev)+1
            for i in range(length):
                if i == 0:
                    row.append(1)
                elif i > 0 and i < length-1:
                    row.append(triangle[row_number - 1][i-1]+triangle[row_number - 1][i])
                else:
                    row.append(1)
            triangle.append(row)
            row_number += 1

        for row in triangle:
            print(row)

    pascal(2)
    pascal(5)
    