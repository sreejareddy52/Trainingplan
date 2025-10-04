import csv

employees = ["Alice", "Bob", "Charlie", "David"]
for emp in employees:
    print(emp)

products = {"Pen": 1.5, "Book": 5.0, "Bag": 20.0}
total = sum(products.values())
print("Total Bill:", total)

with open("C:/Users/sreej/Downloads/Sales.csv", "r") as infile:


    reader = csv.reader(infile)
    data = [row for row in reader if all(row)]

with open("cleaned_sales.csv", "w", newline="") as outfile:
    writer = csv.writer(outfile)
    writer.writerows(data)


