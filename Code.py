from bs4 import BeautifulSoup as bs
import requests as re
import csv

book_csv = open('book_scrape.csv', 'w')
csv_writer = csv.writer(book_csv)
csv_writer.writerow(['Book Name', 'Book Author', 'Book Type', 'price'])

source = re.get('https://www.powells.com/used').text
soup = bs(source, 'html.parser')

for book_details in soup.find_all('div', class_="book-details"):

    book_name = book_details.a.text
    print(book_name)

    book_author = book_details.find('div', class_="book-author").text
    print(book_author)

    book_type = book_details.find('div', class_="book-type").text
    print(book_type)

    prices = book_details.find('div', class_="book-price")

    reg_price = prices.find('div', class_="reg-price").text
    print(reg_price)

    print()
    csv_writer.writerow([book_name, book_author, book_type, reg_price])

book_csv.close()