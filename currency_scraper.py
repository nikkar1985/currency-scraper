import requests
from bs4 import BeautifulSoup
import json

# Η σελίδα που θα κάνουμε scrap (Yahoo Finance Currencies)
URL = "https://finance.yahoo.com/currencies"
headers = {'User-Agent': 'Mozilla/5.0'}

response = requests.get(URL, headers=headers)
    soup = BeautifulSoup(response.text, 'html.parser')
    
    rates = {}
    # Το Yahoo χρησιμοποιεί πλέον data-test="indicator-value" για τις τιμές
    rows = soup.find_all('tr')
    for row in rows:
        cols = row.find_all('td')
        if len(cols) >= 3:
            name = cols[1].text.strip()  # Το όνομα (π.χ. EUR/USD)
            price = cols[2].text.strip() # Η τιμή
            if "/" in name: # Κρατάμε μόνο τα ζεύγη νομισμάτων
                rates[name] = price

    # Κρατάμε μόνο τα πρώτα 5 για να είναι καθαρό το dashboard
    final_rates = dict(list(rates.items())[:5])

    with open('currencies.json', 'w') as f:
        json.dump(final_rates, f)
