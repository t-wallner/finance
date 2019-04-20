import sys
sys.path.append('../')
import data_importer as di
import pandas_datareader._utils as dr_utils
import datetime as dt
import unittest
import unittest.mock
import io

class data_importer(unittest.TestCase):

	def test_run_importer_when_dates_invalid_raises_value_error(self):
		start_date = dt.datetime(2019,1,2)
		end_date = dt.datetime(2019,1,1)
		ticker_list = ["test"]

		self.assertRaises(ValueError, di.run_importer, ticker_list, start_date, end_date )

	@unittest.mock.patch('sys.stdout', new_callable=io.StringIO)
	def test_run_importer_when_ticker_invalid_raises_remote_data_error(self, mock_stdout):
		start_date = dt.datetime(2019,1,1)
		end_date = dt.datetime(2019,1,5)
		ticker_list = ["asdkjfas"]

		di.run_importer(ticker_list, start_date, end_date)

		self.assertEqual(mock_stdout.getvalue(), "No data fetched for symbol asdkjfas using YahooDailyReader\nTicker is invalid\n")


if __name__ == '__main__':
    unittest.main()