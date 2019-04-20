import pandas as pd 
import pandas_datareader.data as web
import pandas_datareader._utils as dr_utils
import datetime as dt
import os

path_ticker_data = "ticker data"
api_yahoo = "yahoo"

def run_importer(ticker_list, start_date, end_date):
	""" Runs the importer which scrapes and saves to csv all ticker data"""
	if start_date > end_date:
		raise ValueError('start date must be an earlier date than end date')

	for ticker in ticker_list:
		try:
			df = scrape_stock_data(ticker, start_date, end_date)
			export_df_to_csv(df, ticker)
		except dr_utils.RemoteDataError as error:
			print(error)
			print("Ticker is invalid")
		else:
			print("Successfully scraped {0} from {1} for dates {2} to {3}"
				.format(ticker, api_yahoo, start_date, end_date))

def scrape_stock_data(ticker, start_date, end_date):
	""" Scrapes stock data from api and returns as dataframe. """
	return web.DataReader(ticker,api_yahoo,start_date,end_date)

def export_df_to_csv(df, file_name):
	""" Exports to csv to enable access to data locally. """
	full_file_name = file_name + ".csv"
	df.to_csv(os.path.join(path_ticker_data,full_file_name))

def read_csv_to_df(ticker):
	""" Reads the locally stored csv and returns as df"""
	file_path = os.path.join(path_ticker_data,ticker)
	return pd.read_csv(file_path + ".csv", parse_dates = True, index_col = 0)


