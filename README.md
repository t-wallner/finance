# finance
This is a fun project that scrapes ticker data from the web, does a little analysis and plots the results

It is very helpful to import all ticker data using the data_importer like the following:

start_date = dt.datetime(2020,1,1)
end_date = dt.datetime(2019,1,1)
ticker_list = ["JPM"]
run_importer(ticker_list, start_date, end_date)

Then, once the data is saved locally, one can use the read_csv_to_df method in data_importer. This saves a lot of time if there is a lot of ticker data.

