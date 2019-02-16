scores = 'chinese=70,math=90,english=80'
x = dict(item.split("=") for item in scores.split(","))
print(x)
print(x.get('chinese'))