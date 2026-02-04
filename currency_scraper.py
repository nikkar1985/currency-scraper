import requests
from bs4 import BeautifulSoup
import json

# Η σελίδα που θα κάνουμε scrap (Yahoo Finance Currencies)
URL = "https://finance.yahoo.com/currencies"
headers = {'User-Agent': 'Mozilla/5.0'}

try:
    response = requests.get(URL, headers=headers)
    soup = BeautifulSoup(response.text, 'html.parser')
    
    # Ψάχνουμε τα στοιχεία στη σελίδα (αναζήτηση βάσει κλάσης)
    # Σημείωση: Τα ονόματα των classes αλλάζουν συχνά στο Yahoo
    rates = {}
    
    # Παράδειγμα για EUR/USD
    rows = soup.find_all('tr')
    for row in rows[:5]: # Παίρνουμε τις πρώτες 5 ισοτιμίες
        cols = row.find_all('td')
        if len(cols) > 1:
            name = cols[1].text
            price = cols[2].text
            rates[name] = price

    with open('currencies.json', 'w') as f:
        json.dump(rates, f)
    print("Currency data scraped!")
except Exception as e:
    print(f"Error: {e}")
