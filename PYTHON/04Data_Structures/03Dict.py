product = {
  "name": "Laptop", 
  "brand": "Dell", 
  "price": 1200, 
  "specs": {
     "processor": "Intel i7",
     "ram": "16GB",
     "storage": "512GB"
  }
 }

print(product["price"])
print(product["specs"]["ram"])


for key, value in product.items():
    print(key,value)

print (product.values())

print (product.get("gpu"))

