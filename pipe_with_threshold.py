import pandas as pd
from functools import partial

data = {
    'Name': ["Rajeev", None, "Neha", "Sahithi", "Ritik"],
    'Age': [22, 23, None, 22, None],
    'City': ["Hyderabad", "Vijayawada", None, None, "Nellore"]
}

df = pd.DataFrame(data)

def fill_missing(df):
    return df.fillna("Unknown")

def filter_min_age(df, min_age=20):

    df['Age'] = pd.to_numeric(df['Age'], errors='coerce')

    return df[df['Age'] >= min_age]

def print_info(df):
    print("\nData types:")
    print(df.dtypes)
    print("\nNull counts:")
    print(df.isnull().sum())
    return df

filter_min_age_with_threshold = partial(filter_min_age, min_age=22)

df_cleaned = (df.pipe(fill_missing)
                .pipe(filter_min_age_with_threshold)
                .pipe(print_info))

print("\nFinal cleaned DataFrame:")
print(df_cleaned)
