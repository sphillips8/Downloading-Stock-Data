import requests
from datetime import datetime
import time

# User input
ticker = input("Enter the ticker symbol: ")
from_date = input('Enter start date in mm/dd/yyy format: ')
to_date = input('Enter end date in mm/dd/yyyy format: ')


# Converts date to datetime format
from_datetime = datetime.strptime(from_date, '%m/%d/%Y')
to_datetime = datetime.strptime(to_date, '%m/%d/%Y')


# Converts datetime to string format
start = from_datetime.strftime('%Y%m%d')
end = to_datetime.strftime('%Y%m%d')


# Converts datetime to epoch
from_epoch = int(time.mktime(from_datetime.timetuple()))
to_epoch = int(time.mktime(to_datetime.timetuple()))


# URL to request data
url = f"https://query1.finance.yahoo.com/v7/finance/download/{ticker}?period1={from_epoch}&period2={to_epoch}&interval=1d&events=history&includeAdjustedClose=true"

# Allows web scraping / simulates web browser
headers = {"User-Agent": "Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/88.0.4324.96 Safari/537.36"} 

# Requests content
content = requests.get(url, headers=headers).content

# Writes data to .csv file
print(f'Saving data to {ticker}_{start}_{end}.csv')
with open(f'{ticker}_{start}_{end}.csv', 'wb') as file:
  file.write(content)