import json

x = '{"name":"john", "age":18}'
person = json.loads(x)

print(type(person['name']))
print(person['name'])
print(type(person['age']))
print(person['age'])