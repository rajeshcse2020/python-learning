def hello(x):
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
    # y = input("Enter the value \n")
    # print("Hello World")
    # print(f"Hellow world {10*10} {x} {y}")
    # if float(y) > 0:
    #     print("posstive number")
    # else:
    #     print("negative number")
    # # while y != 10.0 :
    # #     print("test")
    # for x in range(1,5,2):
    #     print(x)
hello(36)