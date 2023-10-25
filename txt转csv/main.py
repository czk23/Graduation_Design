import csv

with open('test.txt', 'r', encoding='utf-8') as f_input, open('output.csv', 'w', newline='', encoding='utf-8') as f_output:
    csv_output = csv.writer(f_output)
    for line in f_input:
        csv_output.writerow([line.strip()])
