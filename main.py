import csv
data=[]
#Reading the csv file and storing the data from the csv file into a list called 'data'
with open ("archive_dataset.csv","r") as f:
    csvreader=csv.reader(f)
    for row in csvreader :
        data.append(row)

#Storing all the headers into a var called headers
headers=data[0]
#All the planet data into a var called planet_data
planet_data=data[1:]

#Converting all the planet names into lowercase
for data_point in planet_data:
    data_point[2]=data_point[2].lower()

#Sorting the planet names in alphabetical order
planet_data.sort(key=lambda planet_data:planet_data[2])

#Creating a csv file called 'archive_dataset_sorted' and filling in the headers and rows with planet_data in alphabetical order.
with open ("archive_dataset_sorted.csv","a+") as f:
    csvwriter=csv.writer(f)
    csvwriter.writerow(headers)
    csvwriter.writerows(planet_data)

#Removing the blank lines in the csv file
with open ("archive_dataset_sorted.csv") as input, open ("archive_dataset_sorted1.csv","w", newline="") as output:
    writer=csv.writer(output)
    for row in csv.reader(input):
        if any(field.strip() for field in row):
            writer.writerow(row)