import pandas as pd

def transform_data(json_data):

    # If the API return empty list, return empty DataFrame with the expected columns
    if not json_data:
        return pd.DataFrame(columns=["data", "valor"])

    # Transforming result in DataFrame

    df = pd.DataFrame(json_data)

    # Tranforming column value data type and errors = NaN

    df["valor"] = pd.to_numeric(df["valor"], errors="coerce")

    # Transforming column date data type to brazil format and errors = NaN

    df["data"] = pd.to_datetime(df["data"], format="%d/%m/%Y", errors="coerce")

    # Removing duplicate values

    df = df.drop_duplicates()

    # Removing empty fields, holidays, days with no price quotes, etc.

    df = df.dropna()

    return df