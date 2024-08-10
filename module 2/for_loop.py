a="apple"
for i in a:
    print(i)
else:
    print("loop ended")
b=1
for i in "banana":
    if i == "n" :
        print("n found","in",b,"rd iteration.")
        break # if now we want to search again we dont use break
    else:
        b+=1