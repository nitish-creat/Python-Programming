def avg(*num):
    print(type(num))
    sum=0
    for i in num:
        sum+=i
    print("avg is:",sum/len(num))

avg(2,3,4,5,6,7,8)