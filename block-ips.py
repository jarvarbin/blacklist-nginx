import csv

# Read in the blacklist IPs from a CSV file
blacklist_ips = []
with open('blacklist_ips.csv') as csv_file:
    csv_reader = csv.reader(csv_file, delimiter=',')
    for row in csv_reader:
        blacklist_ips.append(row[0])

# Open the nginx configuration file
with open('nginx.conf', 'r+') as nginx_file:
    # Read in lines from the configuration file
    contents = nginx_file.readlines()
    # Find the beginning of the blacklist section
    start_index = 0
    for i, line in enumerate(contents):
        if line.strip() == "# Start of blacklist":
            start_index = i
    # Find the end of the blacklist section
    end_index = 0
    for i, line in enumerate(contents):
        if line.strip() == "# End of blacklist":
            end_index = i
    # Insert the blacklist IPs
    for ip in blacklist_ips:
        contents.insert(end_index, 'deny ' + ip + ';\n')
        end_index += 1
    # Write to the nginx configuration file
    nginx_file.seek(0)
    nginx_file.writelines(contents)
    nginx_file.truncate()

print("Blacklist IPs successfully added to nginx configuration file!")
