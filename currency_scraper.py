import yfinance as yf
import json
import os

# Λίστα με τα ζεύγη
pairs = ["EURUSD=X", "JPY=X", "GBPUSD=X", "AUDUSD=X"]
rates = {}

print("Starting scraping...")

for pair in pairs:
    try:
        ticker = yf.Ticker(pair)
        # Χρησιμοποιούμε το 'currentPrice' ή το 'last_price'
        info = ticker.fast_info
        price = info['last_price']
        
        # Καθαρισμός ονόματος
        display_name = pair.replace("=X", "")
        if len(display_name) == 6:
            display_name = f"{display_name[:3]}/{display_name[3:]}"
            
        rates[display_name] = round(price, 4)
        print(f"Found {display_name}: {price}")
    except Exception as e:
        print(f"Error for {pair}: {e}")

# Αν η λίστα είναι άδεια, βάλε dummy δεδομένα για να μην είναι κενό το JSON
if not rates:
    rates = {"Status": "No data found", "Check": "Manual Run"}

# Αποθήκευση
with open('currencies.json', 'w') as f:
    json.dump(rates, f, indent=4)

print("File currencies.json created successfully!")
