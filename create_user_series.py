import pandas as pd

ages = pd.Series([22, 23, 23, 22, 25, 22, 20, 25, 26, 22],
                 index=["Rajeev", "Ganesh", "Neha", "Sahithi", "Ritik",
                        "Anvitha", "Bhavesh", "Chanukya", "Sameeksha", "Snehitha"])

print(ages)
