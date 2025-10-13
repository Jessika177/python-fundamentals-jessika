import pandas as pd

# data
data = {
    "Name": ["Rajeev", "Ganesh", "Neha", "Sahithi", "Ritik", "Anvitha", "Bhavesh", "Chanukya", "Sameeksha", "Snehitha"],
    "Age": [22, 23, 23, 22, 25, 22, 20, 25, 26, 22],
    "City": ["Hyderabad", "Vijayawada", "Tirupathi", "Uravakonda", "Nellore", "Chennai", "Odissa", "Bangalore", "Kolkata", "Hyderabad"],
    "Email": ["rajeev@email.com", "ganesh@email.com", "neha@email.com", "sahithi@email.com", "ritik@email.com",
              "anvitha@email.com", "bhavesh@email.com", "chanukya@email.com", "sameeksha@email.com", "snehitha@email.com"],
    "JoinDate": ["2023-07-15", "2023-07-20", "2023-08-01", "2023-08-08", "2023-08-12",
                 "2023-09-02", "2023-09-19", "2023-10-03", "2023-10-10", "2023-10-18"]
}

# data frame
df = pd.DataFrame(data)

df.to_csv("users.csv", index=False)

# Print
print("CSV file 'users.csv' created successfully!")
