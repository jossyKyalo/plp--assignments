# Importing libraries
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import requests

# 1. NumPy 
numbers = np.arange(1, 11)  
mean_value = np.mean(numbers)
print("NumPy Array:", numbers)
print("Mean of Array:", mean_value)

# 2. Pandas 
data = {
    "Name": ["Alice", "Bob", "Charlie", "David"],
    "Age": [25, 30, 35, 40],
    "Score": [85, 90, 88, 92]
}
df = pd.DataFrame(data)
print("\nPandas DataFrame:\n", df)
print("\nSummary Statistics:\n", df.describe())

# 3. Requests
response = requests.get("https://api.coindesk.com/v1/bpi/currentprice.json")
if response.status_code == 200:
    bitcoin_data = response.json()
    price_usd = bitcoin_data["bpi"]["USD"]["rate"]
    print("\nCurrent Bitcoin Price (USD):", price_usd)
else:
    print("\nFailed to fetch data from API")

# 4. Matplotlib 
x = [1, 2, 3, 4, 5]
y = [2, 4, 6, 8, 10]

plt.plot(x, y, marker='o')
plt.title("Simple Line Graph")
plt.xlabel("X-axis")
plt.ylabel("Y-axis")
plt.grid(True)
plt.show()
