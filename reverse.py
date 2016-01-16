__author__ = 'ronanpiercehiggins'



def reverse(num):

    newArr = [int(i) for i in str(num)]
    newnewArr = sorted(newArr)
    lis = []

    for i in reversed(newnewArr):
        lis.append(i)

    newVar = int(''.join([ "%d"%x for x in lis]))

    return  newVar




var = reverse(14954)

print int(var)







