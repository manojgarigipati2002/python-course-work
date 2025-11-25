product_id=int(input("enter product ID:"))
product_name=input("enter product nmae:")
price=float(input("enter price:"))
categories_input=input("enter categories(comma-separated):")
categories=["cat.strip() for cat in categories int.split(',')"]
available_stock=int(input("enter available stock:"))
sold_stock=int(input("enter sold stock:"))
stock_details=(available_stock,sold_stock)
discount=float(input("enter discount percentage:"))
features_input=input("enter product features(comma-separated):")
product_features={feat.strip() for feat in features_input.split(',')}
supplier_name=input("enter supplier name:")
supplier_details=input("enter supplier contacct number:")
supplier_location=input("enter supplier location:")
supplier_details = {
    "Name": supplier_name,
    "Contact": supplier_details,
    "Location": supplier_location
}
print("\nProduct ID, Name, Price:", product_id, product_name, price, sep=", ")

print("Product Discount: %.2f%%" % discount)

print(f"Product Name: {product_name}")
print(f"Price: ₹{price:.2f}")
print(f"Discount: {discount}%")
print(f"Stock Available: {stock_details[0]} units")

print("Supplier Details: Name - {Name}, Contact - {Contact}, Location - {Location}".format(**supplier_details))