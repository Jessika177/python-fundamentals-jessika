import pandas as pd

data = {
    'Name': ["Rajeev", "Ganesh", "Neha", "Sahithi", "Ritik",
             "Anvitha", "Bhavesh", "Chanukya", "Sameeksha", "Snehitha"],
    'Age': [22, 23, 23, 22, 25, 22, 20, 25, 26, 22],
    'City': ["Hyderabad", "Vijayawada", "Tirupathi", "Uravakonda", "Nellore",
             "Chennai", "Odissa", "Bangalore", "Kolkata", "Hyderabad"]
}
df = pd.DataFrame(data)

# boolean flags
print("Users with Age > 22:")
print(df[df['Age'] > 22])

print("\nUsers with Age between 22 and 25:")
print(df[df['Age'].between(22, 25)])
