import pandas as pd

data = {
    'Name': ["Rajeev", "Ganesh", "Neha", "Sahithi", "Ritik", "Anvitha", "Bhavesh", "Chanukya", "Sameeksha", "Snehitha"],
    'Age': [22, 23, 23, 22, 25, 22, 20, 25, 26, 22],
    'City': ["Hyderabad", "Vijayawada", "Tirupathi", "Uravakonda", "Nellore", "Chennai", "Odissa", "Bangalore", "Kolkata", "Hyderabad"]
}

df = pd.DataFrame(data, columns=['Name', 'Age', 'City'])

# slicing rows by posi
print("First 3 rows:")
print(df.iloc[0:3])

print("\nFirst 3 rows - names only:")
print(df.iloc[0:3]['Name'])

# slicing by column
print("\nAll ages:")
print(df['Age'])

# slicing multiple columns for rows 2 to 5
print("\nRows 2 to 5 (Age and City):")
print(df.loc[2:5, ['Age', 'City']])
