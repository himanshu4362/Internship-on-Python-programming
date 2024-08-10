money=int(input("Enter your money amount:"))
obj1=int(input("enter your first object price :"))
obj2=int(input("enter your second object price :"))
obj3=int(input("enter your third object price :"))
obj4=int(input("enter your fourth object price :"))
obj5=int(input("enter your fifth object price :"))

sum = obj1+obj2+obj3+obj4+obj5

print("your total expense is ",sum,"and you have left",(money-sum))