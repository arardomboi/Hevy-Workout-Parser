def readCSV(file):
    with open(file, 'r') as f:
        reader = csv.reader(f)
        data = list(reader)
    return data
