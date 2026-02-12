


import pandas as pd

# Create a dictionary (data)
data = {
    "Name": ["Nitish", "Rahul", "Aman"],
    "Age": [21, 22, 20],
    "Marks": [85, 90, 78]
}

# Convert dictionary to DataFrame
df = pd.DataFrame(data)

# Print the DataFrame
print(df)
