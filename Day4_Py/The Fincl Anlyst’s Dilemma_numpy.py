import numpy as np  
np.random.seed(42)

stock_prices = np.random.randint(100,501, size = (30,5))
print("Stock_price: \n", stock_prices)

average_prices = np.mean(stock_prices, axis =0)

max_price = np.max(stock_prices)
max_position = np.where(stock_prices == max_price)
max_day = max_position[0][0]+1
max_company = max_position[1][0]+1

print("\n Highest price:", max_price,"\n max_day: ", max_day,"\n max_company",max_company)

min_price = np.min(stock_prices)
max_price_overall = np.max(stock_prices)
normalized_prices = (stock_prices-min_price)/(max_price-min_price)

print("\n min_price:", min_price, "\n max_price_overall: ", max_price_overall, "\nnormalized_prices:\n", normalized_prices)

risky_days = {}

for i in range (30):
    stocks_below_200 = []
    
    for price in stock_prices[i]:
        if price<200:
            stocks_below_200.append(price)

    if len(stocks_below_200)>0:
        risky_days[f"Day {i+1}"] = stocks_below_200
        
print("\nStock Prices Over 30 Days")
print("Day    Company 1  Company 2  Company 3  Company 4  Company 5")
for i in range(30):
    print(f"Day {i+1:<2}  {stock_prices[i, 0]:<10}{stock_prices[i, 1]:<10}{stock_prices[i, 2]:<10}{stock_prices[i, 3]:<10}{stock_prices[i, 4]:<10}")

print("\nAverage Stock Prices")
for i in range(5):
    print(f"Company {i+1}: ${average_prices[i]:.2f}")

print("\nHighest Stock Price Recorded")
print(f"Highest Price: ${max_price}")
print(f"Day: {max_day}")
print(f"Company: {max_company}")

print("\nNormalized Stock Prices")
print("Day    Company 1  Company 2  Company 3  Company 4  Company 5")
for i in range(30):
    print(f"Day {i+1:<2}  {normalized_prices[i, 0]:<10.2f}{normalized_prices[i, 1]:<10.2f}{normalized_prices[i, 2]:<10.2f}{normalized_prices[i, 3]:<10.2f}{normalized_prices[i, 4]:<10.2f}")

print("\nRisky Investment Days (Stock price below $200)")
if risky_days:
    for day, stocks in risky_days.items():
        print(f"{day}: {stocks}")
else:
    print("No risky investment days found.")