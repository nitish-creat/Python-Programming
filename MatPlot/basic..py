import matplotlib.pyplot as plt

# print(matplotlib.__version__)

months = [1,2,3,4,5]
sales = [100,150,200,250,300]

# plt.plot(months, sales)
# plt.title("Monthly Sales Growth")
# plt.xlabel("Month")
# plt.ylabel("Sales")
# plt.show()

subjects = ["Math", "Science", "English"]
marks = [85, 90, 75]

# plt.bar(subjects, marks)
# plt.title("Student Marks")
# plt.xlabel("Subjects")
# plt.ylabel("Marks")
# plt.show()


data = [10,20,20,30,30,30,40,50,60]

# plt.hist(data, bins=5)
# plt.title("Data Distribution")
# plt.xlabel("Values")
# plt.ylabel("Frequency")
# plt.show()

x = [1,2,3,4,5]
y = [2,4,5,4,5]

# plt.scatter(x, y)
# plt.title("Relationship between X and Y")
# plt.xlabel("X values")
# plt.ylabel("Y values")
# plt.show()

x = [1,2,3,4]
y1 = [10,20,30,40]
y2 = [15,25,35,45]

# plt.plot(x, y1, label="Product A")
# plt.plot(x, y2, label="Product B")

# plt.title("Product Comparison")
# plt.xlabel("X")
# plt.ylabel("Sales")
# plt.legend()
# plt.show()

# plt.figure(figsize=(8,5))
# plt.plot(x, y1)
# plt.show()

# plt.subplot(1,2,1)
# plt.plot(x, y1)
# plt.title("Plot 1")

# plt.subplot(1,2,2)
# plt.plot(x, y2)
# plt.title("Plot 2")

# plt.show()