__author__ = 'ronanpiercehiggins'



items = [1,2,3,4,5]

def myFunc(x):
    return x * 2


var = list(map(myFunc, items))

print var

print map((lambda x: x * 2), items)

myArr = ['hello', 'yo', 'how']
index = 0


for i in myArr:
    var = "var" + str(index)
    print i
    print var
    index += 1

