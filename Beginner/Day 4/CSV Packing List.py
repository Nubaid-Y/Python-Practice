import csv

data = [
  ['Item', 'Quantity'],
  ['Blender', 2],
  ['Posters', 30],
  ['Shoes', 2]
]

try:
    with open("packing_list.csv", "r", encoding="utf8") as file:
        reader = csv.reader(file)
        for row in reader:
            print(row)

except FileNotFoundError:
    with open("packing_listV2.csv", "w", newline = '') as file:
        writer = csv.writer(file)
        writer.writerow(data)
