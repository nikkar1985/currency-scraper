import requests
from bs4 import BeautifulSoup
import json

URL = "https://finance.yahoo.com/currencies"
headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36'
}

try:
    response = requests.get(URL, headers=headers)
    soup = BeautifulSoup(response.text, 'html.parser')
    
    rates = {}
    # Ψάχνουμε όλες τις σειρές του πίνακα
    rows = soup.find_all('tr')
    
    for row in rows:
        cells = row.find_all('td')
        if len(cells) >= 3:
            # Το όνομα είναι συνήθως στο 2ο κελί και η τιμή στο 3ο
            name = cells[1].text.strip()
            price = cells[2].text.strip()
            
            # Φιλτράρουμε μόνο τα γνωστά ζεύγη
            if any(pair in name for pair in ["EUR/USD", "USD/JPY", "GBP/USD", "AUD/USD"]):
                rates[name] = price

    if not rates:
        raise Exception("No rates found. Yahoo might have changed structure.")

    with open('currencies.json', 'w') as f:
        json.dump(rates, f)
    print("Success! Data saved.")

except Exception as e:
    print(f"Error detail: {e}")
    # Αν αποτύχει, φτιάξε ένα dummy αρχείο για να μη σπάει η HTML
    with open('currencies.json', 'w') as f:
        json.dump({"Status": "Error fetching live data"}, f)
