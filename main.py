import requests
from bs4 import BeautifulSoup
import sqlite3

conn = sqlite3.connect('ipo.db')
c = conn.cursor()
c.execute('''CREATE TABLE IF NOT EXISTS ipo_data (
             S_N INTEGER PRIMARY KEY,
             Symbol TEXT,
             Company TEXT,
             Units REAL,
             Price REAL,
             Opening_Date TEXT,
             Closing_Date TEXT,
             Status TEXT
             )''')


url = 'https://www.sharesansar.com/'
response = requests.get(url)
soup = BeautifulSoup(response.content, 'html.parser')
table = soup.find('div',class_='border-tbl auctionhmins').find('table', class_="table table-hover table-striped table-bordered compact").find('tbody')

for row in table.find_all('tr'):
    cells = row.find_all('td')
    symbolno = cells[0].text.strip()
    symbol = cells[1].text.strip()
    company = cells[2].text.strip() 
    units = cells[3].text.strip()
    price = cells[4].text.strip()
    opening_date = cells[5].text.strip()
    closing_date = cells[6].text.strip()[:10]
    status = cells[7].text.strip()
    c.execute("INSERT INTO ipo_data (Symbol, Company, Units, Price, Opening_Date, Closing_Date, Status) VALUES (?, ?, ?, ?, ?, ?, ?)",
              (symbol, company, units, price, opening_date, closing_date, status))
    

conn.commit()
conn.close()


