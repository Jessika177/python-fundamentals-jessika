import pandas as pd

data = {
    'Name': ["Rajeev", None, "Neha", "Sahithi", "Ritik"],
    'Age': [22, 23, None, 22, None],
    'City': ["Hyderabad", "Vijayawada", None, None, "Nellore"]
}

df = pd.DataFrame(data)

def fill_defaults(value):
    if pd.isna(value):
        return "Unknown"
    else:
        return value

df_cleaned = df.apply(lambda col: col.apply(fill_defaults))

print(df_cleaned)

