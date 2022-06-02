import csv

with open('phoneCalls.csv', 'r') as fin:
    reader = csv.reader(fin, delimiter = ",")
    headers = next(reader)

    for row in reader:
        print(row)
        from_subsr = int([0])
        if from_subsr not in call_dict_sum:

        calls_dict_sum[from_subsr] += int(row[3])
