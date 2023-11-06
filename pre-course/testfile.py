header = ("date", "item", "price")
content = [
    ("2020-02-07", "Milk", "26.5"),
    ("2020-02-08", "Water", "7"),
    ("2020-02-08", "Mask", "20"),
    ("2020-02-08", "Lays", "10"),
    ("2020-02-08", "Rice", "6")
]

file = open('products.csv', 'w')
file.write(",".join(header) + "\n")

for row in content:
  file.write(",".join(row) + "\n")

file.close()

with open("products.csv", "r") as f:
  product = f.readlines()

print(product)