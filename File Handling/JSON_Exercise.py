# Please read the instructions carefully and write your script here:
# You need to:
# - read data from csv_file.txt
# - process data and convert them into a single JSON object
# - store the JSON object into json_file.txt
# Your code starts here:
import json 

file = open("csv_file.txt","r")

lines = file.readlines() 
lines = [line.strip() for line in lines]

file.close()

json_object = []

for line in lines:
    club,city,country = line.split(',') #separating on the basis of commas 
    curr = {
        'club':club,
        'country':country,
        'city': city
    }

    json_object.append(curr)


file = open("json_file.txt","w")

json.dump(json_object,file)
file.close()


'''
CSV File 

Manchester United,Manchester,UK
    Real Madrid,Madrid,Spain
    Juventus,Turin,Italy

json_file.txt

[{"club": "Manchester United", "country": "UK", "city": "Manchester"}, {"club": "Real Madrid", "country": "Spain", "city": "Madrid"}, {"club": "Juventus", "country": "Italy", "city": "Turin"}]

'''