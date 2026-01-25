#GLOBAL VARIABLE
# x=10
# def my_function():
#     #LOCAL VARIABLE
#     y=5
#     print("inside the function, local variable y:",y)
#     print("inside the function, global variable x:",x)
# my_function()
# #OUTSIDE THE FUNCTION
# print("outside the function, global variable",x)
#print("outside the function, global variable",y) #this will raise error because y is local to the function



'''counter=10
print(counter)
def my_fun():
    global counter
    counter+=1
    print(counter)
my_fun()
my_fun()
my_fun()
print(counter)'''



# message="hello"
# print(message)
# def print_message():
#     message="hey"
#     print(message)
# print_message()
# print(message)



a=2
print(a)
def fun():
    b=10
    print ("global{a}",a)
    print("local{b}",b)
fun()
print(a)