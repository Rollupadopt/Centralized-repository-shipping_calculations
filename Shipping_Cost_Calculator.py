# Shipping Cost Calculator

## Input package weight and shipping rate
weight = float(input("Enter the package weight in kilograms: "))
rate = float(input("Enter the shipping rate per kilogram: "))

## Calculate shipping cost
shipping_cost = weight * rate

## Display the result
print(f"Shipping Cost: {shipping_cost} USD")

# Here is another update by Boonyarit T.
discount = 0.1
get_dis = shipping_cost - (shipping_cost * discount)
remain_val = get_dis
print(f'Price after discount = {remain_val}') 