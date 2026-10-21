# Spotify 2023 – Data Analysis with pandas

This project reads a CSV dataset of Spotify songs, cleans and fixes the incorrect data, and answers four questions about it.

## Dataset

The CSV file comes from Kaggle. Each row is one song. It has null values and some columns with the wrong data types.

## How to run

1. Clone this repository.
2. Install pandas: `pip install pandas`
3. Make sure the dataset is at `data/spotify-2023.csv`.
4. Run: `python main.py`

## Data issues found

I found columns with the wrong data types, null values and duplicate values.

## Decisions

- **key:** null values filled with "C", because the column has 11 of the 12 musical keys and "C" never appears. The null values are most likely the songs in C. This is an assumption, not a fact from the dataset.
- **in_shazam_charts:** null values kept, because 0 already means the song was not on the chart. A null value probably means the data was not collected, and filling it with 0 would mix the two cases. This column is not used in the analysis.
- **Numbers with commas:** I removed the commas before converting the columns to numbers.
- **Date columns:** I merged the three date columns into a single date column.

## Results

The project answers four questions:

- Top 5 most-played songs
- Songs by The Weeknd
- Total streams of an artist, including collaborations
- Top 5 artists by total streams

## Limitations

In the top 5 artists, collaborations are grouped separately. A song by "The Weeknd, Daft Punk" does not count toward The Weeknd, so only solo songs are summed for each ar