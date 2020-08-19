# 28 - Given 1 (float) number via input, calculate the value discounted by 30%.

price = float(input("Enter a (float) value: "))
price -= price * 0.30

print(f"The final price is: {price}")