import yfinance as yf
import json

# Λίστα με τα ζεύγη που θέλουμε
pairs = ["EURUSD=X", "JPY=X", "GBPUSD=X", "AUDUSD=X"]

rates = {}

for pair in pairs:
    try:
        ticker = yf.Ticker(pair)
        # Παίρνουμε την τελευταία τιμή (last price)
        price = ticker.fast_info['last_price']
        # Καθαρίζουμε το όνομα για την HTML (π.χ. από EURUSD=X σε EUR/USD)
        display_name = pair.replace("=X", "")
        if "USD" in display_name and len(display_name) == 6:
             display_name = f"{display_name[:3]}/{display_name[3:]}"
             
        rates[display_name] = round(price, 4)
    except Exception as e:
        print(f"Error scraping {pair}: {e}")

# Αποθήκευση στο JSON
with open('currencies.json', 'w') as f:
    json.dump(rates, f)

print("Data saved successfully!")
