import json 

file = open("friends_json.txt","r") 
file_contents = json.load(file)
file.close()

print(file_contents['friends'][0])

cars = [
    {"make": "Ford","model":"Fiesta"},
    {"make": "Range Rover","model":"Velar"}
]
#writing JSON into a file 

file = open("cars_json.txt","w")
json.dump(cars,file)

my_json_string = '[{"name":"Edward Snowden","Work": "CyberSecurity"}]' 

#loads for string  
person_1 = json.loads(my_json_string) 

print(person_1[0]["name"])


file.close()