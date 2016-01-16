__author__ = 'ronanpiercehiggins'


"""for x in 'Aoife':
    print (ord(x))
my_arr = ["h", "y", "w"]


result = list(map(ord, my_arr))
print result"""

result = [x for x in 'Aoife']
print result


result = [len(x) for x in 'Aoife' if ord(x) > 60]
print result