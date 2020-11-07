cost_price = float(input())
selling_price = float(input())

if selling_price > cost_price:
    print("Profit")
elif selling_price < cost_price:
    print("Loss")
else:
    print("Neither")

