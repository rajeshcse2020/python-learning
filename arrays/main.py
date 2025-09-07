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

def numberarray():
    x = [1,2,3,4,5,6,7]
    sum: int =0
    start: int = int(input("start index: "))
    end: int = int(input("end Index: "))
    for i in range(start+1,end+1):
       # print(i)
        sum = x[i]+ sum
    print(f"Total Sum is {sum}")

# hello();
numberarray()