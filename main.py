import pandas as pd
import webbrowser
import os

daily_rates: pd.DataFrame = pd.read_csv("https://www.ecb.europa.eu/stats/eurofxref/eurofxref.zip", compression="zip")
historical_rates: pd.DataFrame = pd.read_csv("https://www.ecb.europa.eu/stats/eurofxref/eurofxref-hist.zip", compression="zip")

def mean_exchange_rate(rates_list) -> float:
    return sum(rates_list) / len(rates_list)
    
data: dict = {
    "USD": [daily_rates[" USD"][0], mean_exchange_rate(historical_rates["USD"].tolist())],
    "JPY": [daily_rates[" JPY"][0], mean_exchange_rate(historical_rates["JPY"].tolist())],
    "GBP": [daily_rates[" GBP"][0], mean_exchange_rate(historical_rates["GBP"].tolist())],
    "SEK": [daily_rates[" SEK"][0], mean_exchange_rate(historical_rates["SEK"].tolist())],
}

df: pd.DataFrame = pd.DataFrame(data, index=["Today's Rate", "Average Rate"]).T  # transpose
html: str = df.to_html(border=1)

with open("exchange_rates.html", "w") as file:
    file.write(html)
    
file_path: str = os.path.abspath("exchange_rates.html")
webbrowser.open(f"file://{file_path}")