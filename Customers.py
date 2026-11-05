print("--- Exercise 1 ---")
customer={
    "name":"Alice",
    "email":"alice@example.com",
    "tier":"Gold",
    "ytd_spend": 12400


}
print(customer["name"])
print(customer["email"])
print(customer["tier"])
print(customer["ytd_spend"])

print("--- Exercise 2 ---")
customer["phone"]="813-555-0142"
print(customer)
customer["tier"]="platinum"

print(customer)
del customer ["email"]

print(customer)


print(customer.get("email", "Email not found"))

print("---Exercise 3---")

print(customer.get("email", "Email not found"))

try:
    print(customer["email"])
except KeyError as error:
    print(f"keyError caught: {error}")

print("--- Exercise 4 ---")

for key, value in customer.items():
    print(f"{key}: {value}")

for item in customer:
    print(item)

print("exercise 5 ---")
tier_discounts={"bronze":0,
                "silver":0.05,
                "gold":0.10,
                "platinum":0.15}
purchase=200
discount_rate=tier_discounts.get(customer["tier"], 0)
final_price=purchase * (1-discount_rate)

print("Tier: {customer['tier']}")
print(f"discount: {discount_rate *100:.0f}%")
print(f"final price: ${final_price:.2f}")

print("--- Exercise 6 ---")
customers=[
    {"name": "Bob", "tier": "silver", "ytd_spend": 3200},
    {"name": "Carol", "tier": "gold", "ytd_spend": 8700},
    {"name": "Dave", "tier": "bronze", "ytd_spend": 450},
    
]

for record in customers:
    rate=tier_discounts.get(record["tier"], 0)
    discount=300 * rate
    print(f"Name: {record['name']}, : {record['tier']},: ${discount:.2f}")

print("--- Exercise 7 ---")
catalog= {
"widget A": {"price": 9.99, "stock": 150},
"Gadget C": {"price": 49.99, "stock": 8},
}

for product, details in catalog.items():
    if details["stock"] < 20:
        print(f"LOW STOCK: {product} - only {details['stock']} left in stock!")

print("--- Exercise 8 ---")
transactions=[
    {"region": "South", "amount": 300},
    {"region": "North", "amount": 150},
    {"region": "South", "amount": 200},
    
]
sales_by_region={}
for sale in transactions:
    region=sale["region"]
    sales_by_region[region]=sales_by_region.get(region, 0) + sale["amount"]
print(sales_by_region)

for region in sorted(sales_by_region):
    print(f"{region}: ${sales_by_region[region]}")