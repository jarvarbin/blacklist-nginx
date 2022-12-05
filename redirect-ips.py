
import csv

# open the csv file
with open('ip_list.csv') as csv_file:
    csv_reader = csv.reader(csv_file, delimiter=',')
    line_count = 0

# loop through the csv to write the nginx configuration
    for row in csv_reader:
        if line_count == 0:
            line_count += 1
        else:
            ip = row[0]
            print("location / {" )
            print("  if ($remote_addr = \"" + ip + "\") {")
            print("    return 301 https://www.google.com;")
            print("  }")
            print("}")
            print("")
            line_count += 1
