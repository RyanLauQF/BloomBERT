import csv
import re


new_file_name = 'cleaned_file.csv'
curr_file = 'cleaning.csv'

# Label for current data
blooms_field = 'Apply'
rows = []

with open(curr_file, 'r') as file:
    csvFile = csv.reader(file)

    for line in csvFile:
        if len(line) == 0:
            continue
        # remove numbers and punctuations
        s = re.sub('[^a-zA-Z ]+', '', line[0])
        # remove spaces
        s = (re.sub(' +', ' ', (s.replace('\n', ' ')))).strip()
        # lower case
        s = s.lower()

        rows.append([s, blooms_field])

    file.close()

with open(new_file_name, 'w', newline='') as outfile:
    # creating a csv writer object
    csvwriter = csv.writer(outfile)
    csvwriter.writerows(rows)

    file.close()

