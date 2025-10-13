import pandas as pd

data = {
    'Name': ["Rajeev", "Ganesh", "Neha"],
    'Age': ['22', '23', '23'],
    'JoinDate': ['2023-07-15', '2023-07-20', '2023-08-01']
}

df = pd.DataFrame(data)

df['Age'] = pd.to_numeric(df['Age'])

df['JoinDate'] = pd.to_datetime(df['JoinDate'])

print(df.dtypes)

print(df)
