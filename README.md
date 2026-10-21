# ETL Pipeline with the Central Bank of Brazil API

This project is an ETL pipeline that extracts data from the Central Bank of Brazil API, transforms it with Python and pandas, and loads it into a PostgreSQL database with incremental loading.

## Dataset

The Central Bank of Brazil API returns a JSON with a date and a value for each day of the series.

## How to run

1. Clone this repository.
2. Install the requirements: `pip install -r requirements.txt`
3. Add your PostgreSQL settings to the `.env` file.
4. Run: `python main.py`

## Data issues found

- Dates come in the Brazilian format, so I converted them to a date type with pandas.
- Values come with the wrong data type, so I converted them with pandas.
- The API returns some records with empty values, so I removed them with `dropna`.

## Decisions

- **Incremental load:** the data first goes to a staging table, which is compared with the final table. New dates are inserted, and if a value changed, only the value is updated. The date is the unique key.

## Results

The pipeline can run any number of times without duplicating data. It only updates values that changed.

## Limitations

The pipeline runs only one series at a time, so it can't store two different series in the same table.