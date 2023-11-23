import os
import pandas as pd
import matplotlib.pyplot as plt

# Get the absolute path to the directory of the script
script_directory = os.path.dirname(os.path.abspath(__file__))

# Define the relative path to the CSV file from the script's directory
csv_file_path = os.path.join(script_directory, "..", "avocado.csv")

# Read data from the CSV file
data = pd.read_csv(csv_file_path)

# Print the column names
print(data.columns)

date_column = "Date"
average_price_column = "AveragePrice"

# Assuming your CSV file has columns 'Date' and 'AveragePrice'
dates = data[date_column]
average_prices = data[average_price_column]

# Create a bar chart
plt.bar(dates, average_prices, color="skyblue")
plt.xlabel("Date")
plt.ylabel("Average Price")
plt.title("Avocado Average Price Over Time")
plt.xticks(rotation=45, ha="right")

# Show the plot
plt.show()
