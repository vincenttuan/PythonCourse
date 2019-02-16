import json

x = '{"name":"john", "age":18, "profile":{"w":60.0, "h":170.0}}'
person = json.loads(x) # json string to dict
print(type(person))
print(person['profile']['w'])

#----------------------------------------------------------------
y = '[{"name":"john", "age":18, "profile":{"w":60.0, "h":170.0}}, ' \
    '{"name":"john", "age":18, "profile":{"w":70.0, "h":180.0}}]'
personList = json.loads(y) # json string to dict
print(type(personList))
print(personList)

for person in personList:
    print(person['profile']['w'])



