def hello():
    array_test = ["xyz","apple","banana","kiwi"]
    array_test.sort()
    array_test.append("fruit")
    array_test.pop(3)
    array_test.reverse()
    #array_test.clear()
    for x in range(len(array_test)):
        print(array_test[x])

    for x in array_test:
        print(x)

hello()