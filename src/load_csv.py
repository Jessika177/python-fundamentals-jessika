import pandas as pd

def load_and_print_csv():
    df = pd.read_csv('../user.csv')
    print(df)

if __name__ == "__main__":
    load_and_print_csv()

