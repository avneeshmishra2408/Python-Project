book = {}

book['Tom'] = {
    'Name' : 'Tom',
    'Address' : 'Gwalior',
    'Phone' :  9213823872
}
book['Bob'] = {
    'Name' : 'Bob',
    'Address' : 'Mumbai',
    'Phone' : 7423684545
}


import json
s = json.dumps(book)
# print(s)

# with open("c://label//book.txt", "w" ) as f:
#     f.write(s)
#
# f = open("c://label//book.txt", "r")
# s = f.read()
# print(s)

book = json.loads(s)
print(book)
