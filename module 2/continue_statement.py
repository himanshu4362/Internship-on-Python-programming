for i in range(1,10):
    if i == 5 or i ==7:
        continue 
    print(i)

# this is an infinite loop 
# when the i is 5 then the infinite loop starts 
# and it will print nothing only checking if statement and it found it is true so it will continue 
# means do nothing and again checks the if statement and again found it is true so infinite loop s

i = 1 
while i < 10 :
    if i == 5:
        continue
    print(i)
    i += 1
