import csv


# with open('utilities\loanapp.csv') as csvFile:
#     csvReader=csv.reader(csvFile,delimiter=',')
#     print(type(csvReader),id(csvReader))
#     # for x in csvReader:
#     #     print(x)

with open('utilities\loanapp.csv','a') as wFile:
    csvW=csv.writer(wFile)
    csvW.writerow(["Kavya","Approved"])
    # print(list(csvReader))

with open('utilities\loanapp.csv') as csvFile:
    csvReader=csv.reader(csvFile,delimiter=',')
    print(type(csvReader),id(csvReader))
    for x in csvReader:
        print(x)


