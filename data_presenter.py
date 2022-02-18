import csv

# open_file = open("CupcakeInvoices.csv")
# for line in open_file:
#     print(line)

# type_a = 0
# type_b = 0
# type_c = 0


# for row in open_file:
#     item = row.rstrip("/n").split(",")
#     for value in item:
#         if value == "Chocolate":
#             type_a += 1
#         elif value == "Vanilla":
#             type_b += 1
#         elif value == "Strawberry":
#             type_c += 1 

# print("Chocolate")
# print("Vanilla")
# print("Strawberry")


with open("CupcakeInvoices.csv", "r") as csv_file:
    csv_reader = csv.reader(csv_file, delimiter=",")
    for lines in csv_reader:
     print(lines[2])    


     

csv_file = csv.reader(open("CupcakeInvoices.csv"))

dist = 0
for row in csv_file:
    _dist = row[4]
    _dist2 = row[3]
    try:
        _dist = float(_dist)
        _dist2 = float(_dist2)
    except ValueError:
          _dist = 0 
          _dist2 = 0

    total = _dist * _dist2
   
    print(total)           





csv_file = csv.reader(open("CupcakeInvoices.csv"))

dist = 0
for row in csv_file:
    _dist = row[4]
    try:
        _dist = float(_dist)
    except ValueError:
          _dist = 0 

    dist += _dist
    print(dist + _dist)           





# open_file.close()    