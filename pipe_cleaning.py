import pandas as pd

data = {
    'Name': ["Rajeev", None, "Neha", "Sahithi", "Ritik"],
    'Age': [22, 23, None, 22, None],
    'City': ["Hyderabad", "Vijayawada", None, None, "Nellore"]
}

df = pd.DataFrame(data)

def fill_missing(df):
    return df.apply(lambda col: col.fillna("Unknown"))

def print_info(df):
    print("\nData types:")
    print(df.dtypes)
    print("\nCounts of missing values:")
    print(df.isnull().sum())
    return df

df_cleaned = (df.pipe(fill_missing)
                .pipe(print_info))

print("\nCleaned DataFrame:")
print(df_cleaned)
