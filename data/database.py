import pandas as pd

import os
import sys

sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), "..")))

from db.mysql import engine

def load_data_to_df(sql_query:str):
    with engine.connect() as conn:
        df = pd.read_sql(sql_query, conn)
    return df

if __name__ == "__main__":
    # Example usage
    res = load_data_to_df("SELECT * FROM summary_data_day")
    print(res.head())