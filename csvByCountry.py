import csv

#https://location.services.mozilla.com/downloads

def getstuff(filename):
    with open(filename, "rb") as csvfile:
        reader = csv.reader(csvfile)
        headers = reader.next()
        print(headers)
        print(','.join(headers))
        count = 0
        with open('204.csv', 'w') as the_file:
            the_file.write(','.join(headers) + '\n')
            for row in reader:
                if row[1] == '204':
                    the_file.write(','.join(row) + '\n')
                    continue
        print("Done")

getstuff("MLSCell.csv")
