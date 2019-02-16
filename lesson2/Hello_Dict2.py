dic = {'orange':20, 'apple':100}
print(dic.get('orange'))
print(dic.get('orange', 70))
#print(dic.get('berry', 50))
print(dic.setdefault('berry', 50))

print(dic)
