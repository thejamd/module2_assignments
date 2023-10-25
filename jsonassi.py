#1. Write a program to manipulate string using dumps() & loads()

# d = {}

# d ["gravity"] = {
# "mediator":"gravitons",
# "relative strength" : "1",
# "range" : "infinity"
# }
# d ["weak"] = {
# "mediator":"W/Z bosons",
# "relative strength" : "10^25",
# "range" : "10^-18"
# }
# d ["electromagnetic"] = {
# "mediator":"photons",
# "relative strength" : "10^36",
# "range" : "infinity"
# }
# d ["strong"] = {
# "mediator":"gluons",
# "relative strength" : "10^38",
# "range" : "10^-15"
# }
# print(d)
# # convert dictionary into string using dumps
# import json
# data=json.dumps(d)
# print(data)
# print(type(data))
# print(type(d))
# #write this string into json file
# with open("hello.json","w") as f:
#  f.write(data)
# #read back to dictionary
# with open("hello.json","r") as f:
 
#  data=f.read()
#  d=json.loads(data)
#  print(d)
#  print(d['electromagnetic'])
import json
#2.  Write a program to append an existing json object and display it
#append into a string
# school='{"name":"theja","rollno":31}'
# y={"place":"kdlr"}
# z=json.loads(school)
# z.update(y)
# print(z)
# print(json.dumps(z)) it can be used to convert string into dictionary


# import json

# # JSON data:
# x = '{ "organization":"GeeksForGeeks", "city":"Noida", "country":"India"}'

# # python object to be appended
# y = {"pin":110096}

# # parsing JSON string:
# z = json.loads(x)

# # appending the data
# z.update(y)

# # the result is a JSON string:
# print(json.dumps(z))
m={}
m={
    "student_details":[
        {
            "first_name":"sneha",
            "last_name":"jisnu"
        },
        {
            "first_name":"vismaya",
            "last_name":"aneesh"

        }
    ]
}


print(m)
data=json.dumps(m)
print(data)
with open("my.json","w") as f:
    f.write(data)

def write_json(new_student, filename="./my.json"):
    with open(filename,"r+") as file:
        file_content = json.load(file)
        file_content["student_details"].append(new_student)
        file.seek(0)
        json.dump(file_content, file,indent=4)
        print(file_content)


new_student = {
    "first_name": "Aftab",
    "last_name": "Raza",
    
}

write_json(new_student)