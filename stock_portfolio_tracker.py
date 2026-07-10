# Stock Portfolio Tracker

# Hardcoded stock prices
stock_prices = {
    "AAPL": 180,
    "TSLA": 250,
    "GOOG": 140,
    "MSFT": 320,
    "AMZN": 150
}

total_investment = 0

print("===== STOCK PORTFOLIO TRACKER =====")

num_stocks = int(input("Enter the number of stocks you own: "))

for i in range(num_stocks):
    stock_name = input("\nEnter stock name (AAPL/TSLA/GOOG/MSFT/AMZN): ").upper()
    quantity = int(input("Enter quantity: "))

    if stock_name in stock_prices:
        investment = stock_prices[stock_name] * quantity
        total_investment += investment
        print(f"{stock_name}: ${investment}")
    else:
        print("Stock not found!")

print("\n==============================")
print("Total Investment Value: $", total_investment)

# Save result to a text file
with open("portfolio_result.txt", "w") as file:
    file.write("Stock Portfolio Tracker\n")
    file.write(f"Total Investment Value: ${total_investment}")

print("Result saved to portfolio_result.txt")
