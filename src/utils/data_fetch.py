import yfinance as yf
import os

os.makedirs("data", exist_ok=True)

# Download 1-minute intraday data (limited to past 7 days)
aapl = yf.download("AAPL", interval="1m", period="7d")
msft = yf.download("MSFT", interval="1m", period="7d")

# Save to CSV
aapl.to_csv("data/AAPL_1min.csv")
msft.to_csv("data/MSFT_1min.csv")

print("Data downloaded and saved to /data/")