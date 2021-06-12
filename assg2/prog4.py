#copy contents of one csv file to another
with open('sample1.csv', 'r') as f1, open('sample2.csv', 'w') as f2:
    f2.write(f1.read())