class DictDemo:

    def __init__(self, key, value):
        self.dict = {}
        self.dict[key] = value

    def __getitem__(self, key):
        return self.dict[key]

    def __setitem__(self, key, value):
        self.dict[key] = value

    def __delitem__(self, key):
        del self.dict[key]

    def __len__(self):
        return len(self.dict)

    def __str__(self) -> str:
        return str(self.dict)


dictDemo = DictDemo('h', 170)
print(dictDemo) # __str__
dictDemo['w'] = 60 # __setitem__
print(dictDemo) # __str__
print(dictDemo['h']) # __getitem__
print(len(dictDemo)) # __len__
del dictDemo['h'] # __delitem__
print(dictDemo) # __str__
