import csv
import requests
from bs4 import BeautifulSoup

url = 'https://www.ola.state.md.us/Search/Report?keyword=&agencyId=&dateFrom=&dateTo='
response = requests.get(url, headers={'User-Agent': 'Mozilla/5.0'})
html = response.content

soup = BeautifulSoup(html, features="html.parser")
table = soup.find('tbody')

list_of_rows = []
for row in table.find_all('tr'):
    list_of_cells = []
    for cell in row.find_all('td'):
        if cell.find('a'):
            list_of_cells.append(cell.find('a')['href'])
        text = cell.text.strip()
        list_of_cells.append(text)
    list_of_rows.append(list_of_cells)

list_of_rows = []
for row in table.find_all('tr'):
    list_of_cells = []
    date_cell = row.find_all('td')[0]['data-order'] # '2022-01-27'

    for cell in row.find_all('td'):
        if cell.find('a'):
            list_of_cells.append("https://www.ola.state.md.us" + cell.find('a')['href'])
        text = cell.text.strip()
        list_of_cells.append(text)
    list_of_rows.append(list_of_cells)

outfile = open("./reports.csv", "w", newline='')
writer = csv.writer(outfile)
writer.writerow(["date", "type", "url", "title"])
writer.writerows(list_of_rows)
