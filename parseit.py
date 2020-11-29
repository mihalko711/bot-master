import sqlite3 as sql

import requests
from bs4 import BeautifulSoup

#def main():
def makelist(order):
	conn = sql.connect('drugs.db')
	cur = conn.cursor()

	r = requests.get('https://yandex.ru/health/apteki/search?text=' + order)
	f = open('some', 'w')
	f.write(r.text)
	f.close()

	html = open('some').read()
	soup = BeautifulSoup(html, 'lxml')

	names = soup.find_all('a', {'class': 'pharmacy-search-item__title'})
	prices = soup.find_all('div', {'class': 'pharmacy-product-variants__variant-price'})
	print(names)
	print(prices)


	for a, b in zip(names, prices):
		name = a.get_text()
		price = b.get_text()
		link = a.get('href')
		strong_price = [int(i) for i in price.split() if i.isdigit()][0]

	
		cur.execute("INSERT INTO 'druglist' ('drug_name', 'drug_lower_price', 'strong_price', 'link') VALUES (?,?,?,?)", (name, price, strong_price, link))

	conn.commit()
def showlist():
	conn = sql.connect('drugs.db')
	cur = conn.cursor()

	cur.execute("SELECT * from 'druglist'")
	all_results = cur.fetchall()

	conn.commit()

	return all_results

def clearlist():
	conn = sql.connect('drugs.db')
	cur = conn.cursor()
	
	cur.execute("DELETE FROM 'druglist' WHERE id>0")

	conn.commit()

if __name__ == '__main__':
	main()