"""students = {
    "student1": {
        "name": "Tamim",
         "age": 22
         },
    "student2": {
        "name": "Nargis",
         "age": 23
    },
    "student3": {
        "name": "Shuvo",
         "age": 25
    },
    "student4": {
        "name": "Fairooz",
         "age": 21
    },

}
for key, value in students.items():
    print(key, value)"""


footballers = {
    "player1": {
        "name": "Riyadul Islam Ratul",
        "age": 25,
        "position": "Goalkeeper"
    },
    "player2": {
        "name": "Riyad",
        "age": 20,
        "position": "Goalkeeper"
    },
    "player3": {
        "name": "Riyad",
        "age": 21,
        "position": "Goalkeeper"
    },
    "player4": {
        "name": "Riyad",
        "age": 22,
        "position": "Goalkeeper"
    }, 
    "player5": {
        "name": "Riyad",
        "age": 23,
        "position": "Goalkeeper"
    }
}
"""Print Everything"""
for key, value in footballers["player4"]:
    print(key, value)
# Update a key and print it
footballers["player4"].update({"name": "Golam"})
print(footballers["player4"])
# Add new key
footballers["player4"].update({"size": "xl"})
print(footballers["player4"])
#Remove a item
footballers["player4"].pop("position")
print(footballers["player4"])
# Print only one key
print(footballers["player1"]["name"])
# Print a nested 
print(footballers["player5"])
# Print everything using key
for key in footballers:
    print(footballers[key])