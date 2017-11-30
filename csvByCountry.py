import csv
import os
from sys import argv

#https://location.services.mozilla.com/downloads

print argv

def removeFiles(mydir):
    if not os.path.exists(mydir):
        os.makedirs(mydir)
    else:
        filelist = [ f for f in os.listdir(mydir) if f.endswith(".csv") ]
        for f in filelist:
            os.remove(os.path.join(mydir, f))

def splitCSV(filename):
    with open(filename, "rb") as csvfile:
        reader = csv.reader(csvfile)
        headers = reader.next()
        print(headers)

        vorige = ''
        for row in reader:
            if vorige != row[1]:
                path = 'files/' + row[1] + '.csv'
                the_file = open(path, 'a')
                vorige = row[1]
                if os.stat(path).st_size == 0:
                    the_file.write(','.join(headers)+ '\n')

            string = ','.join(row)
            the_file.write(string + '\n')
                

        print("Done")

removeFiles(argv[2])
splitCSV(argv[1])