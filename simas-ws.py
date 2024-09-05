from bs4 import BeautifulSoup
import requests
import pandas as pd
from dotenv import load_dotenv
import os

load_dotenv()

url = os.getenv('SIMAS_URL')

html_content = requests.get(url).text

soup = BeautifulSoup(html_content, "html.parser")
table = soup.find('table')

headers = [th.get_text() for th in table.find_all('th')]

rows = []
for tr in table.find_all('tr')[1:]:
    cells = [td.get_text() for td in tr.find_all('td')]
    rows.append(cells)

df = pd.DataFrame(rows, columns=headers)

print(df)

# Gerando excel
df.to_excel('simas-relatorio.xlsx', index=False, engine='openpyxl')