import csv
# with open("data.csv","w") as file:
#      writer=csv.writer(file)
#      writer.writerow(["Transcation","User ID", "Product ID"])
#      writer.writerow([22,3,5])
#      writer.writerow([10,7,6])

with open("data.csv") as file:
     reader = csv.reader(file)
     # print(list(reader))

     for row in reader:
          print(row)