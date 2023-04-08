import pickle
import csv
import pandas

# Load the pickled data
with open('Spring2020PolarLowsClean.pkl', 'rb') as f:
    df1 = []
    while True:
        try:
            df1 = pickle.load(f)
        except:
            break

with open('Spring2021PolarLowsClean.pkl', 'rb') as f:
    df2 = []
    while True:
        try:
            df2 = pickle.load(f)
        except:
            break

# Write the data to a CSV file
with open('data.csv', 'w', newline='') as f:
    writer = csv.writer(f)
    writer.writerow(df1.columns)
    # Write each row of data to the CSV file
    for index, row in df1.iterrows():
        if (float(row[4]) < -40 or float(row[4]) > 40) and (float(row[6]) < -40 or float(row[6]) > 40):
            writer.writerow(row)
    
    writer.writerow(df2.columns)
    # Write each row of data to the CSV file
    for index, row in df2.iterrows():
        if (float(row[4]) < -40 or float(row[4]) > 40) and (float(row[6]) < -40 or float(row[6]) > 40):
            writer.writerow(row)