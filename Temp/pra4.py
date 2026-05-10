import matplotlib.pyplot as plt

month = [1,2,3,4,5]
sales = [122,343,434,543,600]

# plt.plot(month,sales)
# plt.title("Monthly sales growth")
# plt.xlabel("month")
# plt.ylabel("sales")
# plt.show()


subject = ["math","eng","science"]
marks = [99,88,90]

# plt.plot(subject,marks)
# plt.title("Student marks")
# plt.xlabel("subject")
# plt.ylabel("marks")
# plt.show()

x = [1,2,3,4]
y1 = [10,20,30,40]
y2 = [15,25,35,45]

plt.plot(x, y1, label="Product a")
plt.plot(x, y2, label="Product a")

plt.title("Mulitple data")
plt.xlabel("X")
plt.ylabel("Sales")
plt.legend()
plt.show()
