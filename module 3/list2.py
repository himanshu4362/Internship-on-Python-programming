list = [1,2,4,5,7,5,3,78,9,7,5,32]
for i in list:
    print(i)
else:
    print("loop ended")

print(len(list))

for i in range(len(list)):
    print(list[i])

# for finding maximum in list
a = 0
for i in list:
    if a < i:
        a = i
print(a)    
# using maximum inbuild function
max(list)

# for finding minimum in the list 
min = 10000
for i in list:
    if min>i:
        min=i
print(min)

list.reverse()
print(list)
