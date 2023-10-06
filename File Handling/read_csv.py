file = open("csv_data.txt","r") 
lines = file.readlines() 

lines = [line.strip() for line in lines[1:]]

my_csv = ','.join(['Bishal','21','Gangtok']) #creating csv 

print(my_csv)

for line in lines:
    print(line) 

