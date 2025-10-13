import pandas as pd

data = {
    'Name': ["Rajeev", "Ganesh", "Neha", "Sahithi", "Ritik", "Anvitha", "Bhavesh", "Chanukya", "Sameeksha", "Snehitha"],
    'Age': [22, 23, 23, 22, 25, 22, 20, 25, 26, 22],
    'City': ["Hyderabad", "Vijayawada", "Tirupathi", "Uravakonda", "Nellore", "Chennai", "Odissa", "Bangalore", "Kolkata", "Hyderabad"]
}

df = pd.DataFrame(data, columns=['Name', 'Age', 'City'])

# display
print("Data types:")
print(df.dtypes)

# first 5 rows
print("\nHead (first 5 rows):")
print(df.head())

# last 5 rows
print("\nTail (last 5 rows):")
print(df.tail())

print("\nDescribe:")
print(df.describe())
