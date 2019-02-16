file = open('demo.txt', 'r', encoding='utf-8')
data = file.read()
print(data)

file = open('demo.txt', 'r', encoding='utf-8')
print(file.readline())
print(file.readline())

file = open('demo.txt', 'r', encoding='utf-8')
list = file.readlines()
for line in list:
    print(line)

print("--------------------------")
file = open('demo.txt', 'r', encoding='utf-8')
list = file.readlines()
for line in list:
    line = line.strip(' \n0')
    print(line)
