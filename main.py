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

html_table = df.to_html(border=1, classes="dataframe")

html_content = f"""
<!DOCTYPE html>
<html lang="en">
<head>
<meta charset="UTF-8">
<title>Exchange Rates</title>
<link rel="stylesheet" href="style.css">
</head>
<body>
<h2>Exchange Rates</h2>
{html_table}
</body>
</html>
"""

html_file = "exchange_rates.html"
with open(html_file, "w", encoding="utf-8") as f:
    f.write(html_content)

file_path = os.path.abspath(html_file)
webbrowser.open(f"file://{file_path}")