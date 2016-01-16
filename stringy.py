__author__ = 'ronanpiercehiggins'


def stringy(size):
    # Good Luck!

    new_string = []

    for i in range(size):

        if i % 2 == 1:

            new_string.append(0)

        else:

            new_string.append(1)


    newVar = str(''.join([ "%d"%x for x in new_string]))





    return newVar



print stringy(5)

