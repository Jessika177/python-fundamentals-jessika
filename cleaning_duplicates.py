import pandas as pd

data = {
    'Name': ["Rajeev", "Ganesh", "Neha", "Neha", "Ritik", "Ganesh", "Bhavesh", "Chanukya", "Sameeksha", "Snehitha"],
    'Age': [22, 23, 23, 23, 25, 23, 20, 25, 26, 22],
    'City': ["Hyderabad", "Vijayawada", "Tirupathi", "Tirupathi", "Nellore", "Vijayawada", "Odissa", "Bangalore", "Kolkata", "Hyderabad"]
}

df = pd.DataFrame(data)

print("Duplicated rows:")
print(df.duplicated())

print("\nNumber of unique names:")
print(df['Name'].nunique())

print("\nDataFrame after dropping duplicates:")
print(df.drop_duplicates())
