a=int(input())
for i in range(65,65+a,1):
    for j in range(i,i+a):
        print(chr(j),end="")
    print()
