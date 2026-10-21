from src.extract import consulting_series_sgs
from src.transform import transform_data
from src.load import loading_data, engine

if __name__ == "__main__":

    raw_data = consulting_series_sgs(11, "01/01/2026", "01/02/2026")

    clean_df = transform_data(raw_data)

    loading_data(clean_df, engine)

    print(clean_df.head())