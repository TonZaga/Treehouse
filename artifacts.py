import csv

# with open('museum.csv', newline='') as csvfile:
#     artreader = csv.reader(csvfile, delimeter='|')
#     rows = list(artreader)
#     for row in rows[:2]:
#         print(', '.join(row))


with open('museum.csv', newline='') as csvfile:
    artreader = csv.reader(csvfile, delimeter='|')
    rows = list(artreader)
    for row in rows[1:3]:
        print(row['group1'])