1# function of finding length
def length(list):
    count = 0
    for i in list:
        count += 1
    return count


list = [24,53,76,87,13,42,53,65,34]
# calling our function
print(length(list))

2# function of finding maximum value in list
def maximum(argument):
    a = 0
    for i in argument:
        if a<i:
            a = i
    return a

#calling our maximum fumction 
print(maximum(list))

3# function for finding sum of all elements of a list
def sum(list):
    s = 0
    for i in list:
        s += i
    return s

lst = [1,2,3,4]
# calling our sum function 
print(sum(lst))

# making fumction of finding power 
def power(value1,value2):
    return value1**value2


# calling our power function 
print(power(5,2))

