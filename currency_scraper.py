import yfinance as yf
import json

# Τα σύμβολα που θέλουμε
pairs = ["EURUSD=X", "USDJPY=X", "GBPUSD=X", "AUDUSD=X"]
rates = {}

for pair in pairs:
    try:
        ticker = yf.Ticker(pair)
        price = ticker.fast_info['last_price']
        
        # Μετατροπή ονόματος για την οθόνη (π.χ. EURUSD=X σε EUR/USD)
        name = pair.replace("=X", "")
        if len(name) == 6:
            name = f"{name[:3]}/{name[3:]}"
            
        rates[name] = round(price, 4)
    except Exception as e:
        print(f"Error for {pair}: {e}")

with open('currencies.json', 'w') as f:
    json.dump(rates, f, indent=4)
